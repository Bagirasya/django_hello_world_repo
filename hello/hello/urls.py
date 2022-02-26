"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from firstapp import views

admin.autodiscover()
urlpatterns = [
    re_path(r'^products/$', views.products),
    path('', views.index, name='home'),
    path('hello_world', views.hello_world),
    path('contact/', views.contact),
    path('details/', views.details),
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about', views.about),
    re_path(r'^admin/', admin.site.urls),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
]