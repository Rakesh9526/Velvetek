from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15,unique=True)
    whatsapp_number = models.CharField(max_length=15)
    reffered_by =models.CharField(max_length=255,null=True)