# Generated by Django 5.0.6 on 2025-03-20 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='slug',
            new_name='product_slug',
        ),
    ]
