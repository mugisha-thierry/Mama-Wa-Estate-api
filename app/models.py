from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
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
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=False):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not password:
#             raise ValueError("Users must have a password")
#         user_obj = self.model(
#             email = self.normalize_email(email)
#         )
#         user_obj.set_password(password)
#         user_obj = is_staff
#         user_obj = is_admin
#         user_obj = is_active
#         user_obj.save()
#         return user_obj

#     def create_staffuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True
#         )
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#             is_admin= True
#         )
#         return user

# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=200, unique=True)
#     active = models.BooleanField()
#     staff = models.BooleanField()
#     admin = models.BooleanField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     #email and password are required by default
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
    
#     objects = UserManager()

#     def __str__(self):              # __class User(AbstractBaseUser):
#     email = models.EmailField(max_length=200, unique=True)
#     active = models.BooleanField()
#     staff = municode__ on Python 2
#         return self.email

    
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin

#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active


# class CustomAccountManager(BaseUserManager):
#     def create_user(self, email, user_name, first_name, password, **other_fields):
#         if not emai:
#             raise ValueError('Please provide an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, user_name, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Super user must be assigned as a staff')

#         if other_fields.get('is_superuser') is not True:
#             raise ValueError('Super user must be assigned as a super user')

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Super user must be assigned as a staff')
        
#         return self.create_user(email, user_name, first_name, password, **other_fields)

class Vendor(models.Model):
    '''
    Model creates user instances of vendors
    '''
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

    def saveVendor(self):
        self.save()

    def deleteVendor(self):
        self.delete()

class Store(models.Model):
    name = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
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

