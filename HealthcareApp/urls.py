"""InframindProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from. import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Logins,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('result/',views.Result,name='result'),
    path('database/',views.Data,name='data'),
    path('delete/<str:pk>/', views.Delete,name="delete_item"),
]
