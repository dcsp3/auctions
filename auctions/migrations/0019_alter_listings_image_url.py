# Generated by Django 4.2.1 on 2023-06-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0018_alter_listings_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="image_url",
            field=models.CharField(
                blank=True,
                default="https://icon-library.com/images/no-image-icon/no-image-icon-13.jpg",
                max_length=500,
                null=True,
            ),
        ),
    ]
