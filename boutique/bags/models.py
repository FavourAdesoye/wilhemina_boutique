from django.db import models

# Create your models here.


class Bag(models.Model):
    title = models.CharField(max_length=250)
    stock = models.IntegerField()
    price = models.FloatField()
    product_image = models.ImageField(
        upload_to='media/images/', default='blank')

    description = models.TextField(blank=True)


def __str__(self):
    return self.title
