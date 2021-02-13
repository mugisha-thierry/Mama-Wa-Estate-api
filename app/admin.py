from django.contrib import admin
from .models import Vendor,Estate
from .models import ProductMerch

# Register your models here.
admin.site.register(ProductMerch)
admin.site.register(Vendor) 
admin.site.register(Estate) 