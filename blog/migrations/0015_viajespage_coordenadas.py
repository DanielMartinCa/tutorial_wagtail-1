# Generated by Django 3.2.11 on 2022-03-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_noticiaspage_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='viajespage',
            name='coordenadas',
            field=models.CharField(blank=True, max_length=500, verbose_name='coordenadas'),
        ),
    ]
