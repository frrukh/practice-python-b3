from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('signup/',views.signup,name='signup'),
    # path('get/',views.get,name='get'),
    path('users/display/',views.display_users,name='display_users'),
    path('user/delete/<int:id>/',views.delete_user,name='delete_user'),
    path('user/edit/<int:id>/',views.edit_user,name='edit_user'),
    path('singup/django/',views.signup_django,name='signup_by_django_form')
]