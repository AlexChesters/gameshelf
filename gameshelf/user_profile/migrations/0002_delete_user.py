# Generated by Django 4.2.4 on 2023-08-25 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
