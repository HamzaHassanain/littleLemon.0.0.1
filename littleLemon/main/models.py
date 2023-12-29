from django.db import models

# Create your models here.
class MenuItemModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images')
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# each booking item will mark one or many menu items
class BookingItemModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date = models.DateField()
    menu_items = models.ManyToManyField(MenuItemModel , related_name='booking_items' , blank=True)
   
    def __str__(self):
        return self.name