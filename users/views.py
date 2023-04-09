from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView
from product.models import Product
from post.models import Drunk
import json

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
    faved = user.faved_p_user.order_by('-day')
    drunk = user.drunk_user.order_by('-day')
    faved_b = user.faved_b_user.order_by("-day")
    drunks = user.drunk_user.all().order_by("-day","-rate")
    faved = user.faved_p_user.order_by("-day")
    faved_b = user.faved_b_user.order_by("-day")
    drunk_type = []
    drunk_data = []
    dic = []
    rate = []

    for item in drunks:
        drunk_type.append(item.product.ptype.ptype)
        rate.append(item.rate)

    for type in list(set(drunk_type)):
        i = 0
        drunk_data.append(drunk_type.count(type))
        dic.append({"x": type, "y":drunk_type.count(type)})
        i += 1

    dic = json.dumps(dic)
    # rate = sum(rate)/len(rate)
    rate = 1

    
    context = {
        'faved_list':faved,
        'object':user,
        'drunk_list':drunk,
        'faved_b_list':faved_b,
        "drunks":drunks,
        "faved":faved,
        "faved_b":faved_b,
        "dic":dic,
        "rate":rate
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
    faved_list = faved
    drunks = user.drunk_user.all().order_by("-day","-rate")
    faved = user.faved_p_user.order_by("-day")
    faved_b = user.faved_b_user.order_by("-day")
    drunk_type = []
    drunk_data = []
    dic = []
    rate = []

    for item in drunks:
        drunk_type.append(item.product.ptype.ptype)
        rate.append(item.rate)

    for type in list(set(drunk_type)):
        i = 0
        drunk_data.append(drunk_type.count(type))
        dic.append({"x": type, "y":drunk_type.count(type)})
        i += 1

    dic = json.dumps(dic)
    # rate = sum(rate)/len(rate)
    rate = 1

    context = {
        "user":user,
        'faved_list':faved_list,
        'drunk_list':drunk,
        'faved_b_list':faved_b,
        "drunks":drunks,
        "faved":faved,
        "faved_b":faved_b,
        "dic":dic,
        "rate":rate
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

def dashboard(request):
    user = request.user
    drunks = user.drunk_user.all().order_by("-day","-rate")
    faved = user.faved_p_user.order_by("-day")
    faved_b = user.faved_b_user.order_by("-day")
    drunk_type = []
    drunk_data = []
    dic = []
    rate = []

    for item in drunks:
        drunk_type.append(item.product.ptype.ptype)
        rate.append(item.rate)

    for type in list(set(drunk_type)):
        i = 0
        drunk_data.append(drunk_type.count(type))
        dic.append({"x": type, "y":drunk_type.count(type)})
        i += 1

    dic = json.dumps(dic)
    rate = sum(rate)/len(rate)

    ctx = {
        "user":user,
        "drunks":drunks,
        "faved":faved,
        "faved_b":faved_b,
        "dic":dic,
        "rate":rate
    }

    return render(request, "./users/dashboard.html", ctx)