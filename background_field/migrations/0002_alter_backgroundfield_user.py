# Generated by Django 4.2.9 on 2024-01-26 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("background_field", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backgroundfield",
            name="user",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
