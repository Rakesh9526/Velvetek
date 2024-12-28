from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminhome,name='adminhome'),
    path('customer/add/',views.add_customer,name='add_customer'),
    path('customer/update/<int:customer_id>/',views.update_customer,name='update_customer'),
    path('customer/delete/<int:customer_id>/',views.delete_customer,name='delete_customer'),
    path('customer/new/',views.new_customer,name='new_customer')
]
