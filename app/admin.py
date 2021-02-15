from django.contrib import admin
from .models import Vendor 
from .models import ProductMerch, Store

# Register your models here.
admin.site.register(ProductMerch)
admin.site.register(Vendor) 
admin.site.register(Store)