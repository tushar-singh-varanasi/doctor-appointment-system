# Generated by Django 4.1.7 on 2023-04-06 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Patient_Name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='Patient_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
