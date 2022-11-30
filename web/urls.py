from django.urls import path
from . import views
from .view import product

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('login_page', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'),
    path('products/create', product.create_view, name='product_create'),
    path('products', product.list_view, name='product_getAll'),
    path('products/<int:id>', product.detail_view, name='product_details'),
    path('products/<int:id>/update', product.update_view, name='product_update'),
    path('products/<int:id>/delete', product.delete_view, name='product_delete')
]
