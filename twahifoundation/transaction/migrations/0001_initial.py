# Generated by Django 2.2 on 2020-09-06 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('contact', '0001_initial'),
        ('stock', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTransactionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Donation', 'Donation'), ('Purchase', 'Purchase'), ('Sell', 'Sell')], max_length=10)),
                ('date_time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('person', models.ForeignKey(blank=True, null='NULL', on_delete=django.db.models.deletion.PROTECT, to='contact.Person')),
                ('products_transaction', models.ManyToManyField(blank=True, through='transaction.ProductTransactionLine', to='stock.Product')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Project', verbose_name='Projet')),
                ('user', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, to='account.User', verbose_name='Responsable')),
            ],
            options={
                'ordering': ['-date_time_created'],
            },
        ),
        migrations.AddField(
            model_name='producttransactionline',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction'),
        ),
    ]
