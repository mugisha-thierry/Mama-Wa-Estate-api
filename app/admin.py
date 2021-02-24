
from django.contrib import admin

from .models import Vendor,Estate,Category,Store
from .models import ProductMerch


# Register your models here.
admin.site.register(ProductMerch)
admin.site.register(Vendor) 
admin.site.register(Estate) 
admin.site.register(Category)
admin.site.register(Store)




