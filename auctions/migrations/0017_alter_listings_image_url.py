# Generated by Django 4.2.1 on 2023-06-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_rename_photo_url_listings_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="image_url",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
