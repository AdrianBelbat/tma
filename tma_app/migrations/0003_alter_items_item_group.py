# Generated by Django 5.0.3 on 2024-03-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_app', '0002_alter_items_options_alter_tmarequests_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_group',
            field=models.CharField(choices=[('test1', 'test1'), ('test2', 'test2')], default='test1'),
        ),
    ]
