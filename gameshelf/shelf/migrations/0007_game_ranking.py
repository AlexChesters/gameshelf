# Generated by Django 4.2.4 on 2023-08-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelf", "0006_alter_game_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="ranking",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
