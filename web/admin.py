from django.contrib import admin
from .models import User, Product

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = User
    extra = 1
admin.site.register(User, UserAdmin)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    extra = 1
admin.site.register(Product, ProductAdmin)

