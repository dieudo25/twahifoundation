# Generated by Django 3.1.1 on 2020-10-14 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_remove_person_created_by'),
        ('transaction', '0004_transaction_with_paypal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contact.person'),
        ),
    ]
