from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

Type = ['Round', 'Square']
Toppings = ['Tomato', 'Broccolini','Potato', 'sausage', 'bacon', 'mushroom', 'mushroom']
Size = ['8','10','12']

def home(request):
    pizzas=Pizza.objects.all()
    context={
        'pizzas':pizzas,
        }
    return render(request,'home.html',context)

def filterTopping(request,pk):
    if pk not in Toppings:
       return  HttpResponse(status=404)
    pizzas=Pizza.objects.filter(topping = pk)
    context={
        'pizzas':pizzas,
        }
    return render(request,'home.html',context)

def filterSize(request,pk):
    if pk not in Size:
       return  HttpResponse(status=404)
    pizzas=Pizza.objects.filter(size = pk)
    context={
        'pizzas':pizzas,
        }
    return render(request,'home.html',context)    

def filterType(request,pk):
    if pk not in Type:
       return  HttpResponse(status=404)
    pizzas=Pizza.objects.filter(type = pk)
    context={
        'pizzas':pizzas,
        }
    return render(request,'home.html',context)


def editPizza(request, pk):
    if request.user.is_authenticated:
        ins=Pizza.objects.get(id=pk)
        form=PizzaForm(instance=ins)
        if(request.method=='POST'):
            form=PizzaForm(request.POST,instance=ins)
            if form.is_valid():
                topping = form.cleaned_data.get("topping")
                type = form.cleaned_data.get("type")
                size = form.cleaned_data.get("size")
                if topping not in Toppings:
                    return  HttpResponse(status=404)
                if type not in Type:
                    return  HttpResponse(status=404)
                if size not in Size:
                    return  HttpResponse(status=404)        
                form.save()
                return redirect('home')
        context={'form':form,
                  } 
        return render(request,'edit.html',context)
    else:
        return redirect('register')


def deletePizza(request,pk):
    if request.user.is_authenticated:
        pizza=Pizza.objects.get(id=pk)
        if(request.method=='POST'):
            pizza.delete()
            return redirect('/')
        context={
            'pizza':pizza,
            }
        return render(request,'delete.html',context)
    else:
        return redirect('home')

# def description(request,pk):
#     course=Courses.objects.get(id=pk)
#     context={
#         'course':course,
#         }
#     return render(request,'description.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=UserCreationForm()
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context={
            'form':form
        }
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
       context={}
       return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')