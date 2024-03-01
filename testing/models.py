from django.db import models

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
    img = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
