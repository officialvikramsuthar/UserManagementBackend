# Generated by Django 4.1.13 on 2023-12-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0002_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
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
                ("user_ip", models.CharField(max_length=15)),
                ("request_details", models.TextField()),
                ("status", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
