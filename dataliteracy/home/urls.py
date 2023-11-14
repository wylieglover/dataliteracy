from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contributors/', views.contributors, name='contributors'),
    path('contact/', views.contact , name='contact'),
    path('reviews/', views.reviews , name='reviews'),
    path('sponsors/', views.sponsors , name='sponsors'),
    path('graphing/', views.graphing , name='graphing'),
    path('barGraphing/', views.barGraphing , name='barGraphing'),
    path('lineGraphing/', views.lineGraphing , name='lineGraphing'),
    path('pieGraphing/', views.pieGraphing , name='pieGraphing'),
    path('missionStatement/', views.missionStatement , name='missionStatement'),
    path('graphing/', views.graphing , name='graphing'),
    path('histoGraphing/', views.histoGraphing , name='histoGraphing')
    path('home/templates/contributors.html', views.contributors, name='contributors'),
    path('home/templates/contact.html', views.contact , name='contact'),
    path('home/templates/reviews.html', views.reviews , name='reviews'),
    path('home/templates/sponsors.html', views.sponsors , name='sponsors'),
    path('home/templates/graphing.html', views.graphing , name='graphing'),
    path('home/templates/barGraphing.html', views.barGraphing , name='barGraphing'),
    path('home/templates/lineGraphing.html', views.lineGraphing , name='lineGraphing'),
    path('home/templates/pieGraphing.html', views.pieGraphing , name='pieGraphing'),
    path('home/templates/missionStatement.html', views.missionStatement , name='missionStatement'),
    path('home/templates/graphing.html', views.graphing , name='graphing'),
    path('home/templates/histoGraphing.html', views.histoGraphing , name='histoGraphing'),
    path('home/templates/bubbleGraphing.html', views.bubbleGraphing , name='bubbleGraphing'),
    path('home/templates/dotGraphing.html', views.dotGraphing , name='dotGraphing'),
    path('home/templates/boxGraphing.html', views.boxGraphing , name='boxGraphing')
]