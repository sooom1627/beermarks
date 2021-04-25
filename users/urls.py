from django.contrib import admin
from django.urls import path, include
from .views import signupFunc, loginFunc, logoutFunc, UserDetail, mypage, UserList, userdetail

urlpatterns = [
    path('signup/',signupFunc, name="signup"), 
    path('login/', loginFunc, name="login"),
    path("logout/", logoutFunc, name="logout"),
    path('mypage/<int:pk>/', mypage, name="mypage"),
    path('userlist/', UserList.as_view(), name="userlist"),
    path('udetexe/<int:pk>/', UserDetail.as_view(), name='udet2'),
    path("udet/<int:pk>/", userdetail, name="udet"),
]