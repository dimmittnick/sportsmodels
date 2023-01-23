# Generated by Django 4.1.4 on 2023-01-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PgaPreds",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("golfer", models.CharField(max_length=64, verbose_name="Golfer")),
                ("position", models.FloatField(verbose_name="Ranking")),
            ],
        ),
    ]