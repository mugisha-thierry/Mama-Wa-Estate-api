from django.db import models

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