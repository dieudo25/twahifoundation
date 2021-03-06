# Generated by Django 2.2.14 on 2020-09-17 16:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20200913_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='yoyoy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='yoyoyo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]
