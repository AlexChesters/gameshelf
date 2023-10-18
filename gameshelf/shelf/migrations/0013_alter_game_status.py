# Generated by Django 4.2.4 on 2023-10-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelf", "0012_alter_game_options_remove_game_ranking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="status",
            field=models.CharField(
                choices=[
                    ("wishlist", "Wishlist"),
                    ("playing", "Currently playing"),
                    ("completed", "Completed"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]