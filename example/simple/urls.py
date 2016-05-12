# example/simple/urls.py

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  url(r'^current_datetime', views.current_datetime, name='current_datetime'),
  url(r'^login/(\w*)', views.login, name='login'),
  url(r'^solution/(?P<item_name>\w+.\w+)/$', views.solution, name='solution')
)
