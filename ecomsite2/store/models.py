from django.db import models
from PIL import Image
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/products/photos')
    price = models.IntegerField()
    sale_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output = (200, 200)
            img.thumbnail(output)
            img.save(self.image.path)

    def savings(self):
        return self.price - self.sale_price
    
    def sub_price(self):
        if self.sale_price:
            return self.sale_price
        else:
            return self.price
    