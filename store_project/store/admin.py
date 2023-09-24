from django.contrib import admin
from .models import Product
from .models import Category ,Order

admin.site.register((Product , Category, Order))
