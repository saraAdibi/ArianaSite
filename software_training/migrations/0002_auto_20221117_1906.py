# Generated by Django 3.1.4 on 2022-11-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software_training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwaretraining',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک'),
        ),
        migrations.AddField(
            model_name='softwaretraining',
            name='url_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان لینک'),
        ),
    ]
