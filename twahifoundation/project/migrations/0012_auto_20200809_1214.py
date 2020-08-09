# Generated by Django 2.2 on 2020-08-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20200809_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('MemberMeeting', 'Meeting between members'), ('FundRainsing', 'Fund rainsing')], default='MemberMeeting', max_length=13),
        ),
    ]
