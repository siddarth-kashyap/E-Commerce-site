
# Register your models here.

from django.contrib import admin
from .models import Category, Product

admin.site.site_header = 'Admin Dashboard'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'product_code', 'image', 'brochure', 'created', 'updated']
    search_fields = ['name', 'description']
    list_filter = ['created', 'updated', 'category']
    list_editable = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
