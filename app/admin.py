from django.contrib import admin
from .models import Vendor 
from .models import ProductMerch

# Register your models here.
admin.site.register(ProductMerch)
admin.site.register(Vendor) 