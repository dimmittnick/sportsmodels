# Generated by Django 4.1.4 on 2023-01-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pga", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pgapreds",
            name="position",
            field=models.IntegerField(verbose_name="Ranking"),
        ),
    ]