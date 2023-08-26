# Generated by Django 4.2.4 on 2023-08-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelf", "0004_alter_game_rating_alter_game_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="platform",
            field=models.CharField(
                choices=[
                    ("steam", "Steam"),
                    ("epic", "Epic"),
                    ("xbox_pc", "Xbox (PC)"),
                    ("gog_galaxy", "GOG Galaxy"),
                    ("pc_standalone", "PC (standalone)"),
                    ("xbox_og", "Xbox (original)"),
                    ("xbox_360", "Xbox 360"),
                    ("xbox_one", "Xbox One"),
                    ("xbox_one_s", "Xbox One S"),
                    ("xbox_series_s", "Xbox Series S"),
                    ("xbox_series_x", "Xbox Series X"),
                    ("ps", "PlayStation"),
                    ("ps2", "PlayStation 2"),
                    ("ps3", "PlayStation 3"),
                    ("ps4", "PlayStation 4"),
                    ("ps5", "PlayStation 5"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
