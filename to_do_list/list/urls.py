"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from list import views

urlpatterns = [
    url(r'^todo/', views.todo, name='todo'),
    url(r'^add/', views.add, name='add'),
    url(r'^deletelist/', views.deletelist, name='deletelist'),
    url(r'^updatelist/', views.updatelist, name='updatelist'),
    url(r'^updatestate/', views.updatestate, name='updatestate'),
]
