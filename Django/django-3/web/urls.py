from django.urls import path
from . import views




urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.display_product, name='display_products'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('signup/', views.signup, name='signup'),


    # path('add/session/', views.add_session, name='add_session'),
    # path('remove/session/', views.remove_session, name='remove_session'),
    # path('check/session/', views.check_session, name='check'),
]