from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('login_page', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'),
    path('create_product', views.create_product, name='create_product')
]
