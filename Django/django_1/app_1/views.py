from django.shortcuts import render
from django.http import HttpResponse

# first of all we have to add the app name in settings.py of project folder.

# first we have to add a urls.py file in the app to make the route of the app manageable.
# we are going to render a text on browser.
''' to do this first we have to import HttpResponse from django.http
and then we have to define a function in our views.py in which we use HttpResponse 
as a function and pass it the text we want to display on the browser.
In django every function we defined have at least single parameter i.e request
like 'self' in oop classes functions.
'''
def home(request):
    return HttpResponse('This is home page.')
