from django.contrib import admin
from django.urls import path, include
from .views import favp, timeline, drunk

urlpatterns = [
     path('favp/', favp, name="favp"),
     path('', timeline, name="timeline"),
     path('drunk/<int:pk>', drunk, name="drunk"),
]















