# Generated by Django 5.0.3 on 2024-04-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0006_product_parentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='breastfeedingdetail',
            name='parentName',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='parentName',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
