# Generated by Django 5.0.4 on 2024-04-26 21:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_bid_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='highest_bidder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Highest Bidder'),
        ),
    ]
