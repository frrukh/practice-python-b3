"""
URL configuration for a_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


'''
the following are the main urls that will be run but we made some urls in 
urls.py of our app in order to get urls first we have to include these
urls in this file.
to do this we have to import include function from django.urls.
'''
from django.contrib import admin
from django.urls import path ,include
'''
the include function is passed in the second parameter of path function 
and it takes a single argument in which we pass the app name and then add 
a dot and then add urls.after this the urls of the given app will include
in this main urls.py file.
'''

'''we can only get the urls of our app py adding app/ before the urls 
defined in the urls.py of app ad we are including these apps on the url 
of app. to directly get the urls of included app we can make the first 
parameter of path empty here like path('',include('app_1.urls'))
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app_1.urls')),
    path('',include('app_2.urls'))

]