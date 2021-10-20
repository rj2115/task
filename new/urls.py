from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('login/', views.logins,name='login'),
    path('register/',views.register,name='signup'),
    path('profile/',views.new_profile,name='profile'),
    path('search/',views.Search,name='search'),
path('logout/',views.ulogout,name='logout'),
path('validations/',views.hi,name='hi')]
