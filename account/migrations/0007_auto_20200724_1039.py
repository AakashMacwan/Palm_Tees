# Generated by Django 3.0.8 on 2020-07-24 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200722_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(message='Enter valid first name', regex='^\\w[a-z|A-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator(message='Enter valid last name', regex='^\\w[a-z|A-Z]+$')]),
        ),
    ]
