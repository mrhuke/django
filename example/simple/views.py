from config import CONFIG
import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from authomatic.adapters import DjangoAdapter
from authomatic import Authomatic

authomatic = Authomatic(CONFIG, 'asuperrandomstring')

def solution(request, item_name):
  fname = os.path.join(settings.PROJECT_ROOT, 'data', item_name)
  return render(request, 'solution.html', {'solution': open(fname).read()})

def current_datetime(request):
  now = datetime.datetime.now()
  t = get_template('current_datetime.html')
  html = t.render(Context({'current_date': now}))
  return HttpResponse(html)

def home(request):
  return HttpResponse('''
      Login with <a href="login/fb">Facebook</a>.<br />
      Login with <a href="login/tw">Twitter</a>.<br />
      <form action="login/oi">
          <input type="text" name="id" value="me.yahoo.com" />
          <input type="submit" value="Authenticate With OpenID">
      </form>
  ''')

def login(request, provider_name):
  response = HttpResponse()
  result = authomatic.login(DjangoAdapter(request, response), provider_name)
  if result:
    response.write('<a href="..">Home</a>')
    if result.error:
      response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
    elif result.user:
      if not (result.user.name and result.user.id):
        result.user.update()
      response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
      response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
      response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
      if result.user.credentials:
        if result.provider.name == 'fb':
          response.write('Your are logged in with Facebook.<br />')
          url = 'https://graph.facebook.com/{0}?fields=feed.limit(5)'
          url = url.format(result.user.id)
          access_response = result.provider.access(url)
          if access_response.status == 200:
            # Parse response.
            statuses = access_response.data.get('feed').get('data')
            error = access_response.data.get('error')
                        
            if error:
              response.write(u'Damn that error: {0}!'.format(error))
            elif statuses:
              response.write('Your 5 most recent statuses:<br />')
              for message in statuses:
                text = message.get('message')
                date = message.get('created_time')
                                
                response.write(u'<h3>{0}</h3>'.format(text))
                response.write(u'Posted on: {0}'.format(date))
            else:
              response.write('Damn that unknown error!<br />')
              response.write(u'Status: {0}'.format(response.status))

        if result.provider.name == 'tw':
          response.write('Your are logged in with Twitter.<br />')
                    
          # We will get the user's 5 most recent tweets.
          url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
                    
          # You can pass a dictionary of querystring parameters.
          access_response = result.provider.access(url, {'count': 5})
                                            
          # Parse response.
          if access_response.status == 200:
            if type(access_response.data) is list:
              # Twitter returns the tweets as a JSON list.
              response.write('Your 5 most recent tweets:')
              for tweet in access_response.data:
                text = tweet.get('text')
                date = tweet.get('created_at')
                                
              response.write(u'<h3>{0}</h3>'.format(text))
              response.write(u'Tweeted on: {0}'.format(date))
                                
            elif response.data.get('errors'):
              response.write(u'Damn that error: {0}!'.\
                  format(response.data.get('errors')))
            else:
              response.write('Damn that unknown error!<br />')
              response.write(u'Status: {0}'.format(response.status))

  return response
