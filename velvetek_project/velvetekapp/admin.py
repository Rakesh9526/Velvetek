from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','name','address','contact_number','whatsapp_number','reffered_by')
admin.site.register(Customer,CustomerAdmin)