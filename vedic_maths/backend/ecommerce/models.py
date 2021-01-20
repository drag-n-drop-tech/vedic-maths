from django.db import models

# Create your models here.

class Product_category(models.Model):
    Category = models.CharField(max_length = 150)
    Category_Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Products(models.Model):
    ProductName = models.CharField(max_length=150)
    ProductCategory = models.ForeignKey(Product_category, on_delete = models.CASCADE)
    NumberInStock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ProductDescription = models.TextField(null=True, blank=True)
    MainImage = models.ImageField(upload_to='products/', null=True, blank=True)
    Image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    Image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    Image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    Image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

