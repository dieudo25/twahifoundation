# Generated by Django 2.2 on 2020-08-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20200811_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='products',
            new_name='products_transfert',
        ),
        migrations.AlterField(
            model_name='productstocktransfert',
            name='transfert_type',
            field=models.CharField(choices=[('RECEPTION', 'Reception'), ('DELIVRY', 'Delivry')], default='RECEPTION', max_length=10),
        ),
    ]
