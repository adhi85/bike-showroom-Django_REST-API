from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    itemsinStock = models.CharField(max_length=200)
    colorsAvailable = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class bikes(models.Model):
    modelNumber = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    warranty =  models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    bikeCategory = models.ForeignKey(Category,on_delete = models.CASCADE)

    def __str__(self):
        return self.modelNumber
