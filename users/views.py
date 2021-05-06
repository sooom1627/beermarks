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

def userdetail(request, pk):
    user = User.objects.get(pk=pk)
    products = Product.objects.all()
    faved = user.faved_p_user.order_by('-day')
    drunk = user.drunk_user.order_by('-day')
    faved_b = user.faved_b_user.order_by("-day")
    
    context = {
        'faved_list':faved,
        'object':user,
        'drunk_list':drunk,
        'faved_b_list':faved_b
    }
    
    return render(request, 'users/udet.html', context)  

class UserList(ListView):
    model = User
    template_name = "./users/ulist.html"

@login_required
def mypage(request):
    user = request.user
    faved = user.faved_p_user.order_by("-day")
    drunk = user.drunk_user.order_by("-day")
    faved_b = user.faved_b_user.order_by("-day")
    #faved = product.fav_product.filter(user=request.user)
    faved_list = faved
    context = {
        "user":user,
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
            return redirect("mypage")
        except:
            print("hello")
            newname = request.POST["uname"]
            newudesc = request.POST["udesc"]
            if user.uname != newname:
                user.uname = newname

            if user.udesc != newudesc:
                user.udesc = newudesc
            user.save()

            return redirect("mypage")

    return render(request, "./users/detail_edit.html", context)
