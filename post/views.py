from .models import Favp
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, Brand
from .models import Favp, PostOb, Drunk, Favb, Like
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def timeline(request):
    posts = PostOb.objects.all().order_by('-id')
    products = Product.objects.all()
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
    liked_list=[]
    for post in posts:
        liked = post.like_set.filter(user=request.user)
        if liked.exists():
            liked_list.append(post.id)

    context = {
        "posts":posts,
        "products":products,
        'faved_list':faved_list,
        'drunk_list':drunk_list,
        "liked_list":liked_list
    }
    return render(request, 'post/list.html', context)

@login_required
def newPost(request):
    try:
        product_id = int(request.GET['product_id'])
        brand_id = int(request.GET['brand_id'])
        brands = Brand.objects.all()
        products = Product.objects.all()
        context = {
            "brands":brands,
            "products":products,
            "brand_id":brand_id,
            "product_id":product_id,
        }
    except:
        brands = Brand.objects.all()
        products = Product.objects.all()
        context = {
            "brands":brands,
            "products":products,
        }
        print("hello")

    return render(request, 'post/post.html', context)

@login_required
def favp(request):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=request.POST.get('product_id'))
        user = request.user
        faved = False
        fav = Favp.objects.filter(product=product, user=user)
        obs = PostOb.objects.filter(favp=fav)
        if fav.exists():
            fav.delete()
        else:
            fav.create(product=product, user=user)
            for favs in fav:
                obs.create(favp=favs, drunk=None)
            #obs.save()
            faved=True
        
        context={
            'product_id':product.id,
            'faved':faved,
            'count': product.fav_product.count(),
        }

    # if request.is_ajax():
    return JsonResponse(context)

@login_required
def favb(request):
    if request.method == "POST":
        brand = get_object_or_404(Brand, pk=request.POST.get('brand_id'))
        user = request.user
        faved = False
        fav = Favb.objects.filter(brand=brand, user=user)
        if fav.exists():
            fav.delete()
        else:
            fav.create(brand=brand, user=user)
            faved=True
        
        context={
            'brand_id':brand.id,
            'faved':faved,
            'count': brand.fav_brand.count(),
        }

    # if request.is_ajax():
    return JsonResponse(context)

def drunk(request, pk):
    if request.method == "POST":
        user = request.user 
        #com = request.POST["com"]
        #rate = request.POST["rating"]
        product = Product.objects.get(pk=pk)
        drunk = Drunk.objects.filter(product=product, user=user)
        obs = PostOb.objects.filter(drunk=drunk)
        
        if request.POST["com"]:
            com = request.POST["com"]
        else:
            com = "記録用(Just for Recording)"
            
        try:
            rate = request.POST["rating"]
        except:
            rate = 3

        try: 
            drunk.create(user=user, product=product, com=com, rate=rate)
            for drunks in drunk:
                obs.create(drunk=drunks, favp=None)
            return redirect("detail", pk=pk)
        except IntegrityError:
            return redirect("detail", pk=pk)
    
    return redirect("detail", pk=pk)

def like(request):
    if request.method == "POST":
        post = get_object_or_404(PostOb, pk=request.POST.get('post_id'))
        user = request.user
        liked = False
        like = Like.objects.filter(post=post, user=user)
        if like.exists():
            like.delete()
        else:
            like.create(post=post, user=user)
            liked = True
        
        ctx = {
            'post_id': post.id,
            'liked': liked,
        }
    return JsonResponse(ctx)


def posts(request):
    if request.method == "POST":
        user = request.user 
        product = Product.objects.get(pk=request.POST["product"])
        drunk = Drunk.objects.filter(product=product, user=user)
        obs = PostOb.objects.filter(drunk=drunk)
        
        if request.POST["com"]:
            com = request.POST["com"]
        else:
            com = "記録用(Just for Recording)"

        try:
            rate = request.POST["rating"]
        except:
            rate = 3

        try: 
            postpic = request.FILES["postpic"]
            try: 
                drunk.create(user=user, product=product, com=com, rate=rate, postPic=postpic)
                for drunks in drunk:
                    obs.create(drunk=drunks, favp=None)
                return redirect("timeline")
            except IntegrityError:
                return redirect("timeline")
        except:
            try: 
                drunk.create(user=user, product=product, com=com, rate=rate)
                for drunks in drunk:
                    obs.create(drunk=drunks, favp=None)
                return redirect("timeline")
            except IntegrityError:
                return redirect("timeline")

    
    return redirect("timeline")
        
@login_required
def index(request):
    posts = PostOb.objects.all().order_by('-id')[:4]
    products = Product.objects.all().order_by("-id")[:4]
    brands = Brand.objects.all().order_by("-id")[:4]

    context={
        "posts":posts,
        "products":products,
        "brands":brands
    }

    return render(request, "index.html", context)

def deletePost(request):
    keyNum = int(request.GET['drunk_id'])
    drunk = Drunk.objects.get(pk=keyNum)
    drunk.delete()
    return redirect("timeline")