from django.contrib import admin
from .models import bikes,Category

# Register your models here.

admin.site.register(bikes)
admin.site.register(Category)