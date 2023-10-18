# Generated by Django 4.2.4 on 2023-09-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelf", "0010_alter_game_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="status",
            field=models.CharField(
                choices=[
                    ("wishlist", "Wishlist"),
                    ("unplayed", "Unplayed"),
                    ("playing", "Currently playing"),
                    ("completed", "Completed"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]