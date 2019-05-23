from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from label.models import CatagoryF,CatagoryS

# Create your views here.



class LoginView(View):


    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("userpass")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            cat_f_s = CatagoryF.objects.all()
            return render(request, 'ptlabel.html', dict(cats = cat_f_s))
        else:
            return render(request, 'login.html', dict(msg="用户或密码错误"))

class LogoutView(View):
    """登出逻辑"""

    def get(self, request):
        logout(request)
        from django.urls import reverse
        return HttpResponseRedirect(reverse("login"), {})




