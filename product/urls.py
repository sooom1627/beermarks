from django.contrib import admin
from django.urls import path, include
from .views import Cre, Cre_b, Det, productView, BrandView, searchproduct, BrandDetail, detail
urlpatterns = [
    #path("", List.as_view(), name="list"),
    path("create/", Cre.as_view(), name="create"),
    path("create_b/", Cre_b.as_view(), name="create_b"),
    path("detail/<int:pk>", detail, name="detail"),
    #path("detail2/<int:pk>", detail, name="detail2"),
    path("list/", productView, name="list"),
    path("brand/", BrandView.as_view(), name="brandlist"),
    path("brand/detail/<int:pk>", BrandDetail.as_view(), name="branddetail"),
    path("search/", searchproduct, name="search"),
    path("search-list,", searchproduct, name="search-list")
]