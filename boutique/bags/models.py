from django.db import models

# Create your models here.


class Bag(models.Model):
    title = models.CharField(max_length=250)
    stock = models.IntegerField()
    price = models.FloatField()
    cvr_url = models.CharField(max_length=2048)
