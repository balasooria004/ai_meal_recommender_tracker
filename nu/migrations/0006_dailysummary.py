# Generated by Django 5.2.3 on 2025-06-20 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nu", "0005_remove_userprofile_carbs_remove_userprofile_fat_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DailySummary",
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
                ("date", models.DateField()),
                ("total_calories", models.FloatField(default=0)),
                ("total_protein", models.FloatField(default=0)),
                ("total_fat", models.FloatField(default=0)),
                ("total_carbs", models.FloatField(default=0)),
                ("total_fiber", models.FloatField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "date")},
            },
        ),
    ]
