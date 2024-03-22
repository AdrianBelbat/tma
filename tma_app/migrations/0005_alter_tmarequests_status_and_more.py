# Generated by Django 5.0.3 on 2024-03-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_app', '0004_alter_items_unit_of_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmarequests',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In use', 'In use')], default='New', null=True),
        ),
        migrations.AlterField(
            model_name='tmarequests',
            name='unit_of_measurement',
            field=models.CharField(choices=[('Kilogram', 'Kilogram'), ('Miligram', 'Miligram')], default='Kilogram'),
        ),
    ]
