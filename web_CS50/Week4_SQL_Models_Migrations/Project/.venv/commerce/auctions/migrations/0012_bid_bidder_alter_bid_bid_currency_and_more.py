# Generated by Django 5.0.4 on 2024-04-26 21:04

import django.db.models.deletion
import djmoney.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_lot_decription_lot_highest_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', '$ USD')], default='USD', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='lot',
            name='highest_bid',
            field=djmoney.models.fields.MoneyField(blank=True, currency_choices=(('USD', 'USD'),), decimal_places=2, default_currency='USD', max_digits=14, null=True, verbose_name='Highest Bid'),
        ),
    ]
