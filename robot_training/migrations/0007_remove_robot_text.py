# Generated by Django 3.1.4 on 2022-11-17 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot_training', '0006_auto_20221117_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='text',
        ),
    ]
