from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('magazine', views.magazine, name='magazine'),
    path('events', views.events, name='events'),
    path('pictorial', views.pictorial, name='pictorial'),
]