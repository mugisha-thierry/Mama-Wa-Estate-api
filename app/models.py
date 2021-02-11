from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.
class ProductMerch(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)