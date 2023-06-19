# Generated by Django 4.2.1 on 2023-06-18 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_rename_text_comments_comment_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listings",
            name="highest_bid",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="listings",
            name="highest_bidder",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]