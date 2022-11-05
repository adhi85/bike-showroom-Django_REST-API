from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    itemsinStock = models.CharField(max_length=200)
    colorsAvailable = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class bikes(models.Model):
    modelNumber = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=200)
    warranty = models.DateField()
    price = models.IntegerField()
    bikeCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.bikeCategory, self.modelNumber)


class Cart(models.Model):
    cart_id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    bikes = models.OneToOneField(bikes, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
