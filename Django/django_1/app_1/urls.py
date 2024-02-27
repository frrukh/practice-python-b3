'''
In url.py of the app first we have to import path from django.urls in order to
define the url of any function written in views.py file.
'''
from django.urls import path
# After this we have to import the views.py to get it's functions
from . import views

# urlpatterns list is used to define all the urls of the app.
urlpatterns = [
    # the path function takes two parameters 1.route 2.function of that route
    # in django route always ends with forward slash (/)
    path('',views.home)
]