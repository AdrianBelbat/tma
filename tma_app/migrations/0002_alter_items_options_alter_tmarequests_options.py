# Generated by Django 5.0.3 on 2024-03-17 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tma_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='tmarequests',
            options={'verbose_name_plural': 'TmaRequests'},
        ),
    ]
