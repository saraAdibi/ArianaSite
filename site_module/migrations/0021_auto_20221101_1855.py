# Generated by Django 3.1.4 on 2022-11-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0020_acordeon'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='subtitle',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='زیر عنوان'),
        ),
        migrations.AddField(
            model_name='services',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان'),
        ),
    ]
