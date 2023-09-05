from django.db import models
from user.models import CustomUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length = 150)
    product_description = models.TextField()
    product_img = models.ImageField(upload_to = "products/", default = None)
    price = models.CharField(max_length = 20)
    quantity  = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    def __str_(self):
        return self.product_name
    
    
    
class Cart(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete  = models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.user_id.username} | {self.product.product_name}"