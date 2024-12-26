from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            print(f"User authenticated: {user.username}, Role: {user.role}")
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'technician':
                return redirect('technician_dashboard')
            else:
                logout(request)
                return render(request, 'login.html', {'error': 'Unauthorized access'})
        else:
            print("Invalid credentials")
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def technician_dashboard(request):
    return render(request, 'technician_dashboard.html')
