# Generated by Django 4.0 on 2021-12-25 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0010_auto_20211223_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 0, 46, 27, 976611)),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_At',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 26, 0, 46, 27, 975612)),
        ),
    ]