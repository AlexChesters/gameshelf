# Generated by Django 4.2.4 on 2023-08-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shelf", "0007_game_ranking"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="game",
            options={"ordering": ["ranking"]},
        ),
        migrations.AddField(
            model_name="game",
            name="release_date",
            field=models.DateTimeField(null=True),
        ),
    ]
