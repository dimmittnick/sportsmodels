# Generated by Django 4.1.4 on 2023-02-06 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mlb", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hitterpreds",
            name="value",
        ),
    ]