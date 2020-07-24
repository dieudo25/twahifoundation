# Generated by Django 2.2 on 2020-07-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20200724_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=60, unique=True),
        ),
    ]
