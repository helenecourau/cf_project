from django.contrib import admin
from .models import Farmer, Product, Certificate, ProductFarmer

class ProductFarmerInline(admin.TabularInline):
    model = ProductFarmer
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductFarmerInline,)

class FarmerAdmin(admin.ModelAdmin):
    inlines = (ProductFarmerInline,)

admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Certificate)
admin.site.register(ProductFarmer)
