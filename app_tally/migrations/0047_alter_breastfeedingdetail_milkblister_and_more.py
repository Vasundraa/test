# Generated by Django 5.0.3 on 2024-04-23 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0046_alter_breastfeedingdetail_nipplecracks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='milkBlister',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='breastfeedingdetail',
            name='nippleCracks',
            field=models.BooleanField(default=False),
        ),
    ]