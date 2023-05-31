from django.db import models


class Clothes(models.Model):
    title = models.CharField(max_length=250)
    stock = models.IntegerField()
    price = models.FloatField()
    cvr_url = models.CharField(max_length=2048)

    def __str__(self):
        return self.title
