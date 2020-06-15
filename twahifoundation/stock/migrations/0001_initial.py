# Generated by Django 2.2 on 2020-06-15 17:26

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
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Prix')),
                ('image', models.URLField(blank=True, max_length=255, null=True, verbose_name="URL de l'image")),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('is_saleable', models.BooleanField(default=True, verbose_name='Vendable')),
                ('is_purchasable', models.BooleanField(default=True, verbose_name='Achetable')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.Category', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfert_type', models.CharField(choices=[('RECEPTION', 'Réception'), ('RECEPTION', 'Livraison')], default='RECEPTION', max_length=10, verbose_name='Type de transfert')),
                ('quantity', models.PositiveSmallIntegerField(default=None, verbose_name='Quantité')),
                ('transfert_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Product', verbose_name='Produits')),
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
                ('name', models.CharField(default=None, max_length=100, verbose_name='Nom')),
                ('location', models.CharField(max_length=255, null=True, verbose_name='Lieu')),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('is_full', models.BooleanField(default=False, verbose_name='Est rempli')),
                ('products', models.ManyToManyField(through='stock.ProductStock', to='stock.Product')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='productstock',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stock.Stock'),
        ),
    ]
