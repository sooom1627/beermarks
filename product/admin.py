from django.contrib import admin
from .models import Brand, Product, Type, Medium, Locate

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Locate)
admin.site.register(Medium)