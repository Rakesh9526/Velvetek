from django.shortcuts import render

# Create your views here.
def technicianhome(request):
    return render(request,'technician_dashboard.html')