# Generated by Django 2.2 on 2020-08-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20200820_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
            preserve_default=False,
        ),
    ]
