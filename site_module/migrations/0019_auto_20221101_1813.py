# Generated by Django 3.1.4 on 2022-11-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0018_delete_acordeon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='services',
            name='title',
        ),
    ]
