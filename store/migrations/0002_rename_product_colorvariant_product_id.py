# Generated by Django 4.2.3 on 2023-07-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colorvariant',
            old_name='product',
            new_name='product_id',
        ),
    ]
