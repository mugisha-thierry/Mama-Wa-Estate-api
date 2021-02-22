
from django.contrib import admin
from .models import Estate,Category,Cart,Product, CartProduct

from .models import Vendor,Estate,Category,Store,Order


# Register your models here.

admin.site.register(Vendor) 
admin.site.register(Estate) 
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Order)


