# Generated by Django 3.1.4 on 2022-11-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0026_auto_20221115_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mdriver',
            name='mdriver_text',
        ),
    ]
