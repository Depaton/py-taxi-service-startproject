# Generated by Django 4.0.2 on 2024-01-26 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_manufacturer_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='manufactured',
            new_name='manufacturer',
        ),
    ]