from django.contrib import admin
from django.urls import path, include
from .views import  productView, BrandView, searchproduct, BrandDetail, detail, brandDetail

urlpatterns = [
    path("detail/<int:pk>", detail, name="detail"),
    path("list/", productView, name="list"),
    path("brand/", BrandView.as_view(), name="brandlist"),
    path("brand/detail/<int:pk>", brandDetail, name="branddetail"),
    path("search/", searchproduct, name="search"),
    path("search-list,", searchproduct, name="search-list")
]