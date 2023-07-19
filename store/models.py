from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class StoreType(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.name}'
    
class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    store_type = models.OneToOneField(StoreType, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    business_cert = models.CharField(max_length=255)
    ghana_card = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.store_name}'
    
class Category(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    more_images = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    colours = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    quantity = models.CharField(max_length=255)
    total_price = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} ordered'



