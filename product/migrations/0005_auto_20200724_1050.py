# Generated by Django 3.0.8 on 2020-07-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200724_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(default='product/images/not_found.jpg', upload_to='product/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='product/images/not_found.jpg', upload_to='product/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default='product/images/not_found.jpg', upload_to='product/images'),
        ),
    ]