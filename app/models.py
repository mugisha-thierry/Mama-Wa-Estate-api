from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.
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
    profile_pic = models.ImageField(upload_to = 'profile/')

    def __str__(self):
        return self.name

    def saveVendor(self):
        self.save()

    def deleteVendor(self):
        self.delete()   

class ProductMerch(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)