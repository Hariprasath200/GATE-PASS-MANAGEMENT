# Generated by Django 5.0.1 on 2024-05-05 09:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pass", "0009_remove_std_status"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="std",
            name="hod_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="std",
            name="incharge_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("student", "Student"),
                            ("incharge", "Incharge"),
                            ("hod", "HOD"),
                            ("warden", "Warden"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
