from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Estate(models.Model):
    name  = models.CharField(max_length=90)
    location =models.CharField(max_length=800)
    estate_logo = models.ImageField(upload_to="images",default="test.png")
    description = models.TextField()
   

    def create_estate(self):
        self.save()

    def delete_estate(self):
        self.delete()

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


# Create a profile for the vendors

class Vendor(models.Model):
    '''
    Model creates user instances of vendors
    '''
    name = models.CharField(max_length=40)
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.CharField(max_length=40)
    product_type = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to = 'products/')
  

    def __str__(self):
        return self.name

    def saveVendor(self):
        self.save()

    def deleteVendor(self):
        self.delete()

class Store(models.Model):
    name = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    location = models.CharField(max_length=40)

    def saveStore(self):
        self.save()

    def __str__(self):
        return self.name
    
    def deleteStore(self):
        self.delete()

class ProductMerch(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)

