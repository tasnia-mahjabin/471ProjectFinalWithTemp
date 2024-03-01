from django.contrib import admin

# Register your models here.
from testing.models import addData,addProduct,Product

# Register your models here.
admin.site.register(addData)
admin.site.register(addProduct)
admin.site.register(Product)
