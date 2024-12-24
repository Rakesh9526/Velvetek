from django.urls import path
from loginapp import views


urlpatterns = [
    path("",views.home,name="home")
]