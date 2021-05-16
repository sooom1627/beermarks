from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Brand, Product, Type
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from users.models import User
from post.models import Favp
from django.db.models import Q, Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from users.views import OnlyYouMixin
#from django.contrib.auth.mixins import LoginRequiredMixin

def detail(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    avg = product.drunk_product.aggregate(Avg("rate"))
    avg = avg["rate__avg"]
    faved = product.fav_product.filter(user=user)
    faved_list = 0
    if faved.exists():
        faved_list = product.id

    if product.fav_product.filter(user=user):
        faved = True

    context = {
        "object":product,
        "avg":avg,
        'faved_list':faved,
    }
    faved_list = []
    
    return render(request, "./product/detail.html", context)

def brandDetail(request, pk):
    user = request.user
    brand = Brand.objects.get(pk=pk)
    products = brand.brand_n.all()[:4]
    faved_list = 0
    if brand.fav_brand.filter(user=user):
        faved = True
    else:
        faved = False

    context = {
        "object":brand,
        "items":products,
        "faved_list":faved
    }

    return render(request, "./product/detail_b.html", context)
    


@login_required
def productView(request):
    products = Product.objects.all().order_by("-id")
    paginator = Paginator(products, 12)
    page = request.GET.get('page', 1) 
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)

    has_page = pages.has_other_pages
    
    faved_list = []
    for product in products:
        faved = product.fav_product.filter(user=request.user)
        if faved.exists():
            faved_list.append(product.id)
            
    drunk_list=[]
    for product in products:
        drunk = product.drunk_product.filter(user=request.user)
        if drunk.exists():
            drunk_list.append(product.id)
    context = {
        'products':pages,
        'faved_list':faved_list,
        'pages': pages,
        'drunk_list':drunk_list,
    }

    return render(request, 'product/list.html', context)

def brandView(request):
    brands = Brand.objects.all().order_by("-id")
    faved_list = []

    for brand in brands:
        faved = brand.fav_brand.filter(user=request.user)
        if faved.exists():
            faved_list.append(brand.id)
            
    context={
        "object_list":brands,
        "faved_list":faved_list
    }

    return render(request, 'product/list_b.html', context)

def searchproduct(request):
    query = request.GET.get("q")
    ptype = request.GET.get("type")
    brand = request.GET.get("brand")
    products = Product.objects.all()
    faved_list = []
    
    for product in products:
        faved = product.fav_product.filter(user=request.user)
        if faved.exists():
            faved_list.append(product.id)

    if query:
        products_result = Product.objects.filter(
            Q(pname__icontains=query)|
            Q(ptype__ptype_search_index__contains=query)|
            Q(brand__bname_search_index__icontains=query)
        )

        products_result = products_result.order_by("-id")
    else:
        products_result = products

    if ptype:
        products_result = products_result.filter(ptype=ptype)
    else:
        products_result = products_result
    
    
    if brand:
        products_result = products_result.filter(brand=brand).order_by("-id")
    else:
        products_result = products_result

    context = {
        'products':products_result,
        'query':query,
        'faved_list':faved_list,
    }

    return render(request, 'product/search-list.html', context )