# Generated by Django 3.2.3 on 2021-07-05 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_auto_20210705_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_data',
            field=models.DateField(verbose_name=datetime.datetime(2021, 7, 5, 15, 7, 8, 147858, tzinfo=utc)),
        ),
    ]