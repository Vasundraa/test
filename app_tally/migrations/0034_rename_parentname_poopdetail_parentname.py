# Generated by Django 5.0.3 on 2024-04-22 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0033_rename_premature_product_premature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poopdetail',
            old_name='ParentName',
            new_name='parentName',
        ),
    ]
