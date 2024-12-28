from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminhome,name='adminhome'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('new_customer',views.new_customer,name='new_customer')
]
