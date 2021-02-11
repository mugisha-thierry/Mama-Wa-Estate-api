from django.db import models

# Create your models here.
class Vendor(models.Model):
    '''
    Model creates user instances of vendors
    '''
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    product_type = models.CharField(max_length=20)
    