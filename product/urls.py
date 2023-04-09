from django.contrib import admin
from django.urls import path, include
from .views import  productView, searchproduct, detail, brandDetail, brandView

urlpatterns = [
    path("detail/<int:pk>", detail, name="detail"),
    path("list/", productView, name="list"),
    path("brand/detail/<int:pk>", brandDetail, name="branddetail"),
    path("search/", searchproduct, name="search"),
    path("search-list,", searchproduct, name="search-list"),
    path("brand/", brandView, name="brandlist")
]