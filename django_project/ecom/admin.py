from django.contrib import admin

# Register your models here.


from .models import Products , Categories

admin.site.register(Products)

admin.site.register(Categories)
