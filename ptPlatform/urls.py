"""ptPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from .settings import MEDIA_ROOT
import xadmin

from users.views import LoginView, LogoutView
from label.views import GetCatagory, GetAllUnlabeled, NextItem, LabelItem, Status

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('get_cat/', GetCatagory.as_view(), name='get_cat'),
    path('get_unlabeled/', GetAllUnlabeled.as_view(), name='get_unlabeled'),
    path('next_item/', NextItem.as_view(), name='next_item'),
    path('label_item', LabelItem.as_view(), name='label_item'),
    path('status', Status.as_view(), name='status'),
    re_path('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]
