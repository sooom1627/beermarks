from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from product.models import Product
from django.urls import reverse

# Create your views here.

class UserIndex(DetailView):
    model = User
    template_name = "base.html"

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk'] #or user.is_superuser

def signupFunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return redirect("index")
        except IntegrityError:
            return render(request, "signup.html", {"error":"This user is already registerd"})
    return render(request, "./users/signup.html", {})

def loginFunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "./users/login.html", {})
    return render(request, "./users/login.html", {})

def logoutFunc(request):
    logout(request)
    # Redirect to a success page.
    return redirect("login")


def userdetail(request, pk):
    user = User.objects.get(pk=pk)
    products = Product.objects.all()
    fav_objects = user.faved_p_user.order_by('-id')
    faved_list = []
    
    for product in products:
        faved = product.fav_product.filter(user=request.user)
        if faved.exists():
            faved_list.append(product.id)

    context = {
        'faved_list':faved_list,
        'object':user,
        "fav_objects":fav_objects
    }

    return render(request, 'users/udetexe.html', context)  

class UserList(ListView):
    model = User
    template_name = "./users/ulist.html"

@login_required
def mypage(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    faved = user.faved_p_user.order_by("-day")
    drunk = user.drunk_user.order_by("-day")
    faved_b = user.faved_b_user.order_by("-day")
    #faved = product.fav_product.filter(user=request.user)
    faved_list = faved
    context = {
        'products':product,
        'faved_list':faved_list,
        'drunk_list':drunk,
        'faved_b_list':faved_b,
    }

    return render(request, 'users/mypage.html', context)

def userEdit(request):
    user = request.user
    context = {
        "object":user
    }
    if request.method == "POST":
        try:
            print("good bye")
            newname = request.POST["uname"]
            newupic = request.FILES["upic"]
            newudesc = request.POST["udesc"]

            if user.uname != newname:
                user.uname = newname

            if user.upic != newupic:
                user.upic = newupic

            if user.udesc != newudesc:
                user.udesc = newudesc
            
            user.save()
            return redirect("mypage", pk=user.pk)
        except:
            print("hello")
            newname = request.POST["uname"]
            newudesc = request.POST["udesc"]
            if user.uname != newname:
                user.uname = newname

            if user.udesc != newudesc:
                user.udesc = newudesc
            user.save()

            return redirect("mypage", pk=user.pk)

    return render(request, "./users/detail_create.html", context)
