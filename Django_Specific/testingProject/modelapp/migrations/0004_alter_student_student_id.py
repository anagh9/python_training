# Generated by Django 3.2.7 on 2021-12-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]