# Generated by Django 4.1.4 on 2023-01-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nhl", "0004_remove_nhlpreds_blah"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nhlpreds",
            name="date",
            field=models.CharField(
                default="2023-01-28", max_length=64, verbose_name="Date"
            ),
        ),
    ]
