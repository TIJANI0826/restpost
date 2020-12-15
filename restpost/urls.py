"""restpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include,path
from rest_framework import routers
from post import views

from rest_framework import routers
from rest_framework import permissions ,viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
  
    path('post_list',views.post_list,name='post_list'),
    path('post_detail/<int:pk>',views.post_detail,name='post_detail'),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('post',views.post,name='post'),

]