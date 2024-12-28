from django.shortcuts import render,get_object_or_404, redirect
from .models import Customer
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.



def adminhome(request):
    return render(request,'admin_dashboard.html')


def add_customer(request):
    if 'term' in request.GET:
        term = request.GET.get('term', '').strip()
        qs = Customer.objects.filter(contact_number__istartswith=term)
        contact_numbers = [contact.contact_number for contact in qs]
        return JsonResponse(contact_numbers, safe=False)

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        address = request.POST.get('address', '').strip()
        contact_number = request.POST.get('contact_number', '').strip()
        whatsapp = request.POST.get('whatsapp', '').strip()
        referred_by = request.POST.get('referred_by', '').strip()

        if not name or not contact_number:
            messages.error(request, "Name and Contact Number are required.")
            return render(request, 'add_customer.html')

        if Customer.objects.filter(contact_number=contact_number).exists():
            messages.error(request, "A customer with this contact number already exists.")
            return render(request, 'add_customer.html')

        Customer.objects.create(
            name=name,
            address=address,
            contact_number=contact_number,
            whatsapp_number=whatsapp,
            reffered_by=referred_by,
        )

        messages.success(request, "Customer added successfully!")
        customers = Customer.objects.all()
        return render(request, 'new_customer.html', {'success': True, 'customers': customers})

    return render(request, 'add_customer.html')


def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        address = request.POST.get('address', '').strip()
        contact_number = request.POST.get('contact_number', '').strip()
        whatsapp = request.POST.get('whatsapp', '').strip()
        referred_by = request.POST.get('referred_by', '').strip()

        if not name or not contact_number:
            messages.error(request, "Name and Contact Number are required.")
            return render(request, 'update_customer.html', {'customer': customer})

        if Customer.objects.filter(contact_number=contact_number).exclude(id=customer.id).exists():
            messages.error(request, "A customer with this contact number already exists.")
            return render(request, 'update_customer.html', {'customer': customer})

        customer.name = name
        customer.address = address
        customer.contact_number = contact_number
        customer.whatsapp_number = whatsapp
        customer.referred_by = referred_by
        customer.save()

        messages.success(request, "Customer updated successfully!")
        return redirect('new_customer')  

    return render(request, 'update_customer.html', {'customer': customer})


def new_customer(request):
    dict_user={
        'customers':Customer.objects.all()
    }
    return render(request,'new_customer.html',dict_user)
