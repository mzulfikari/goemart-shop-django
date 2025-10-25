from django.contrib import admin
from .models import ProductModel,ProductCategoryModel,ProductImageModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id","title","stock","status","created_date")
    
    
    
@admin.register(ProductCategoryModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_date")
    
    

@admin.register(ProductImageModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id","file","created_date")