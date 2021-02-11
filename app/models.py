from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Estate(models.Model):
    name  = models.CharField(max_length=90)
    location =models.CharField(max_length=800)
    estate_logo = models.ImageField(upload_to="images",default="test.png")
    description = models.TextField()
   

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def __str__(self):
        return f"{self.name}"
