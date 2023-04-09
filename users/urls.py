from django.contrib import admin
from django.urls import path, include
from .views import  dashboard, mypage, UserList, userdetail, userEdit

urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('userlist/', UserList.as_view(), name="userlist"),
    path("udet/<int:pk>/", userdetail, name="udet"),
    path('mypage/useredit',userEdit, name="useredit" ),
    path('dashboard', dashboard, name="dashboard")
]