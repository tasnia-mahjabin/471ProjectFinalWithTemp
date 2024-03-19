from django.db import models
from datetime import datetime 

# Create your model
class addData(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

class addProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    catagory = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    img = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    catagory = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    quantity = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    img = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=50,default="datetime.now()")

    def __str__(self):
        return self.name

class user(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name