# Generated by Django 2.2.14 on 2020-09-15 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200913_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published')], default='Drafted', max_length=10),
        ),
    ]
