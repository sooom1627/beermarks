from django.contrib import admin
from django.urls import path, include
from .views import favp, timeline, drunk, index, favb, newPost, posts

urlpatterns = [
     path('favp/', favp, name="favp"),
     path('timeline', timeline, name="timeline"),
     path('drunk/<int:pk>', drunk, name="drunk"),
     path("", index, name="index"),
     path('favb/', favb, name="favb"),
     path('new-post', newPost, name="newPost"),
     path('create_post/', posts, name="createpost")
]















