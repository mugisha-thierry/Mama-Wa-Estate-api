from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    username = models.CharField("username", unique=True, max_length=255, blank=True)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"

class Vendor(CustomUser):
    '''
    Model creates user instances of vendors
    '''
    is_vendor = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username

    def saveVendor(self):
        self.save()

    def deleteVendor(self):
        self.delete()