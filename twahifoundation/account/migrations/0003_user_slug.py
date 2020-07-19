# Generated by Django 2.2 on 2020-07-18 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200713_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=60, unique=True),
            preserve_default=False,
        ),
    ]
