# Generated by Django 3.1.4 on 2022-10-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
    ]
