# Generated by Django 3.0.5 on 2020-09-02 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
