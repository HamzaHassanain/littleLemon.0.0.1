from django.contrib import admin
from . import models 
# Register your models here.
admin.site.register(models.MenuItemModel)
admin.site.register(models.BookingItemModel)