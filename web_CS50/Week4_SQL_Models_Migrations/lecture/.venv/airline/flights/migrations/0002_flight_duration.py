# Generated by Django 5.0.4 on 2024-04-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
