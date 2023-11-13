from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('missionStatement.html')
  return HttpResponse(template.render())

def contributors(request):
  template = loader.get_template('contributors.html')
  return HttpResponse(template.render())

def sponsors(request):
  template = loader.get_template('sponsors.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def reviews(request):
  template = loader.get_template('reviews.html')
  return HttpResponse(template.render())

def graphing(request):
  template = loader.get_template('graphing.html')
  return HttpResponse(template.render())

def barGraphing(request):
  template = loader.get_template('barGraphing.html')
  return HttpResponse(template.render())

def lineGraphing(request):
  template = loader.get_template('lineGraphing.html')
  return HttpResponse(template.render())

def pieGraphing(request):
  template = loader.get_template('pieGraphing.html')
  return HttpResponse(template.render())