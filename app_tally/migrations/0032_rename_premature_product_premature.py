# Generated by Django 5.0.3 on 2024-04-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0031_remove_product_premature_alter_product_sex_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='premature',
            new_name='Premature',
        ),
    ]
