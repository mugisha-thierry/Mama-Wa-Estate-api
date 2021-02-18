from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from django.contrib.auth.models import User
from django.conf import settings

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
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # contact = models.IntegerField()
    # location = models.CharField(max_length=40)
    # product_type = models.CharField(max_length=20)
    # product_image = models.ImageField(upload_to = 'products/')
  

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


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products" ,null=True, blank=True)
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("M-pesa", "M-pesa"),
    ("Paypil", "Paypal"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)

