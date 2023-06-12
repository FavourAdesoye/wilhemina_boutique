from django.contrib import admin
from .models import Bag


class BagAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock')


# Register your models here.
admin.site.register(Bag, BagAdmin)
