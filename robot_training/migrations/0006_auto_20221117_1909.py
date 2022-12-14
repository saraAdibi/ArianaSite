# Generated by Django 3.1.4 on 2022-11-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot_training', '0005_robot_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک'),
        ),
        migrations.AddField(
            model_name='robot',
            name='url_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان لینک'),
        ),
    ]
