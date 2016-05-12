import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

def home(request):
  filename = os.path.join(settings.PROJECT_ROOT, 'data', 'sample.txt')
  # TODO: Dynamically generate a list of file names.
  return render(request,
                'home.html', 
                {'content': open(filename).read(),
                 'item_list': ['sample.txt', 'bubble.c', 'kmp.cc']})
