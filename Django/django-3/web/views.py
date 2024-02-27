from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.add_product_form import ProductForm
from .models import Product
from django.contrib.sessions.models import Session
from django.contrib import messages

# Importing forms here
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    # return HttpResponse(request.META.get('REMOTE_ADDR'))
    return HttpResponse('the upper line in the code is giving the ip address of the user!')

def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request,'add_product_form.html',{'form':form})
    else:
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('display_products')
        else:
            # return render(request,'test.html',{'form':form})
            return HttpResponse(form.errors)
            return HttpResponse('please enter the valid entries!')


def display_product(request):
    products = Product.objects.all()
    return render(request,'display_products.html',{'products':products})


def edit_product(request,id):
    product = Product.objects.get(pk=id)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'edit_product_form.html',{'form':form,'id':id})
    else:
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('display_products')
        else:
            return HttpResponse(form.errors)

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('display_products')


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        # return HttpResponse(form)
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user registered successfully')
            return redirect('display_products')
        else:
            messages.error(request, 'Invalid entries please try again')
            return redirect('signup')




# using sessions

# def add_session(request):
#     request.session['is_added'] = True
#     return HttpResponse('session added')

# def remove_session(request):
#     request.session.pop('is_added')
#     return HttpResponse('session removed')

# def check_session(request):
#     if 'is_added' in request.session:
#         return HttpResponse(request.session['is_added'])
#     else:
#         return HttpResponse('session not found')
