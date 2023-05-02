from django.contrib import admin
from .models import Product,ProductImages
from .forms import ProductForm

class ProductMultipleImageAdmin(admin.StackedInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMultipleImageAdmin]
    fields = ['product_name','price','category','content']
    list_display = ['product_name','price','category','content']
    form = ProductForm



@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    fields = ['product','photo']
    list_display = ['product','photo']
# admin.site.register(ProductImages,ProductAdmin)