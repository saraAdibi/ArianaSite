# Generated by Django 3.1.4 on 2022-11-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot_training', '0004_auto_20221117_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
