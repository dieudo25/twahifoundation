# Generated by Django 2.2.12 on 2020-08-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_auto_20200815_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='is_subscribed',
        ),
        migrations.AddField(
            model_name='person',
            name='is_subscsribed',
            field=models.BooleanField(default=False, verbose_name='Is subscribed to the newsletter'),
        ),
    ]
