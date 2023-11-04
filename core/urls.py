from django.urls import path
from . import views

urlpatterns = [
path('', views.home,name='home'),
path('academy/', views.academy,name='academy'),
path('university/', views.university,name='university'),
path('specialization/', views.specialization,name='specialization'),
path('contact/', views.contact,name='contact'),
path('events/', views.events,name='events'),
path('about/', views.about,name='about'),
path('team/', views.team,name='team'),
path('blog/', views.blog,name='blog'),
path('activities_blog/', views.activities_blog,name='activities_blog'),
]
