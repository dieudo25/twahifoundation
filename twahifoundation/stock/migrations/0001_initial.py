# Generated by Django 2.2.12 on 2020-08-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.URLField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('is_saleable', models.BooleanField(default=True)),
                ('is_purchasable', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.Category')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductStockTransfert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfert_type', models.CharField(choices=[('RECEPTION', 'Reception'), ('DELIVRY', 'Delivry')], default='RECEPTION', max_length=10)),
                ('quantity', models.PositiveSmallIntegerField(default=None)),
                ('date_time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Product')),
            ],
            options={
                'verbose_name': 'Transfert de produits',
                'verbose_name_plural': 'Transferts de produits',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('is_full', models.BooleanField(default=False)),
                ('products_transfert', models.ManyToManyField(through='stock.ProductStockTransfert', to='stock.Product')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='productstocktransfert',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.Stock'),
        ),
    ]
