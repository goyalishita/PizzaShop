from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('Type/<str:pk>',filterType,name='filterType'),
    path('Size/<str:pk>',filterSize,name='filterSize'),
    path('Topping/<str:pk>',filterTopping,name='filterTopping'),
    path('delete/<str:pk>', deletePizza,name='deletePizza'),
    path('edit/<str:pk>', editPizza,name='editPizza'),
    path('register/', registerPage,name='register'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
]