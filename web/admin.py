from django.contrib import admin
from .models import User, ProductModel


class UserAdmin(admin.ModelAdmin):
    model = User
    extra = 1


admin.site.register(User, UserAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = ProductModel
    extra = 1


admin.site.register(ProductModel, ProductAdmin)
