# Generated by Django 4.2.9 on 2024-01-28 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("background_field", "0002_alter_backgroundfield_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="backgroundfield",
            options={"ordering": ["-id"]},
        ),
    ]
