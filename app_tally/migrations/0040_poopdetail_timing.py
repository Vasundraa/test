# Generated by Django 5.0.3 on 2024-04-22 18:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tally', '0039_breastfeedingdetail_submission_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poopdetail',
            name='timing',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
