from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import User
from .forms.django_form import UserForm
# Create your views here.

def home(request):
    return HttpResponse('hi this is home page.')


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        data = request.POST
        if first_name and email and password and confirm_password and password == confirm_password:
            user = User(first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect('display_users')
        else:
            return HttpResponse('<h1>please enter all the required fields correctly.</h1>')


def display_users(request):
    users = User.objects.all()
    # return HttpResponse(user)
    # return HttpResponse(user[0])
    # return HttpResponse(user[0].id)
    return render(request,'display_users.html',{'users':users})


def delete_user(request,id):
    # user = User.objects.get(id=id)
    # we can also define pk i.e primery key instead of id here like
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('display_users')

def edit_user(request,id):
    user = User.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'edit_user.html',{'user':user})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        if first_name and last_name and email:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('display_users')
        else:
            return HttpResponse('Invalid entries! please enter all fields with valid values.')



def signup_django(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request,'django_form.html',{'user':form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # email = request.POST['email']
            # password = request.POST['password']
            # user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            # user.save()
            # return redirect('display_users')
            # now we are going to save the user automatically using django forms.
            # after making some changes in form now we can save the form automatically after validation.
            # now we only have to save the form and it will be saved to the defined model.
            form.save()
            return redirect('display_users')
        else:
            return HttpResponse('invalid entries!')
# def get(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         data = request.POST
#         if first_name and email and password and confirm_password and password == confirm_password:
#             return render(request , 'get.html' ,{'data' : data})
#         else:
#             return HttpResponse('<h1>please enter all the required fields correctly.</h1>')
#     else:
#         return HttpResponse('<h1 style="color:"red"">Method not allowed.</h1>')
