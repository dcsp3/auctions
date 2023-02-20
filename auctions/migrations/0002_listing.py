# Generated by Django 4.1.5 on 2023-02-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                ("category", models.CharField(max_length=64)),
                ("description", models.CharField(max_length=300)),
                ("bid", models.IntegerField()),
                ("photo_url", models.CharField(max_length=500)),
            ],
        ),
    ]
