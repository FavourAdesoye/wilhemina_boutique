# Generated by Django 4.2 on 2023-06-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='cvr_url',
        ),
        migrations.AddField(
            model_name='bag',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bag',
            name='product_image',
            field=models.ImageField(default='blank', upload_to='media/images/'),
        ),
    ]