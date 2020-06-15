# Generated by Django 2.2 on 2020-06-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('image', models.URLField(blank=True, max_length=255, null=True, verbose_name="URL de l'image")),
                ('description', models.TextField(verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('date_ended', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('TODO', 'TO DO'), ('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN PROGRESS'), ('LATE', 'LATE'), ('DONE', 'DONE')], default='TODO', max_length=11, verbose_name='Statut')),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, null=True, verbose_name='Date de création')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Date limite')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project', verbose_name='Projet')),
                ('users', models.ManyToManyField(to='account.User', verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Tâche',
                'verbose_name_plural': 'Tâches',
                'ordering': ['-date_created'],
            },
        ),
    ]
