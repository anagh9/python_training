# Generated by Django 3.2.7 on 2021-12-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0006_auto_20211223_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
