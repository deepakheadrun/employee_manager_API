# Generated by Django 3.0.5 on 2020-08-25 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=18)),
                ('mobile', models.CharField(blank=True, max_length=18)),
                ('department', models.CharField(blank=True, max_length=60)),
                ('reporting_to', models.CharField(blank=True, max_length=60)),
                ('date_of_joining', models.DateField(blank=True)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('employee_type', models.CharField(blank=True, max_length=30)),
                ('career_goal', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
