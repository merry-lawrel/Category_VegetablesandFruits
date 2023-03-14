from django.db import models

# Create your models here.
class Catsample(models.Model):
    cat_name = models.CharField(max_length=10)
    cat_image = models.ImageField(upload_to='sample', default="null.jpg")

class Prdsample(models.Model):
    prd_name = models.CharField(max_length=10)
    prd_image = models.ImageField(upload_to='simple', default="null.jpg")
    prd_price = models.IntegerField(default=0)
    prd_cat = models.CharField(max_length=10, default='')