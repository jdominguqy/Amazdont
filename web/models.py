from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname


class Users(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + self.surname


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
