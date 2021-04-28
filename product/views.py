from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Brand, Product
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from users.models import User
from post.models import Favp
from django.db.models import Q, Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from users.views import OnlyYouMixin
#from django.contrib.auth.mixins import LoginRequiredMixin

class Cre(CreateView):
    template_name = "./product/create.html"
    model = Product
    fields = ("pName", "bName_p", "pPic", "desc", "pType")
    success_url = reverse_lazy("list")

class Cre_b(CreateView):
    template_name = "./product/create_b.html"
    model = Brand
    fields = ("bName", )
    success_url = reverse_lazy("list")

class Det(DeleteView):
    template_name = "./product/detail.html"
    model = Product

def detail(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    avg = product.drunk_product.aggregate(Avg("rate"))
    avg = avg["rate__avg"]

    context = {
        "object":product,
        "avg":avg
    }

    return render(request, "./product/detail.html", context)


@login_required
def productView(request):
    products = Product.objects.all().order_by("-id")
    paginator = Paginator(products, 9)
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

class BrandView(ListView):
    model = Brand
    template_name = "product/list_b.html"

class BrandDetail(DeleteView):
    model = Brand
    template_name = "product/detail_b.html"

def searchproduct(request):
    query = request.GET.get("q")
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
        products_result = Product.objects.all()

    ctx = {
        'products':products_result,
        'query':query,
        'faved_list':faved_list,
    }

    print(ctx)

    return render(request, 'product/search-list.html', ctx )
       
