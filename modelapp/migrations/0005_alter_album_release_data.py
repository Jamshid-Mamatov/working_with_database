# Generated by Django 3.2.3 on 2021-07-05 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0004_alter_album_release_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
