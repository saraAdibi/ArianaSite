# Generated by Django 3.1.4 on 2022-10-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0006_auto_20221029_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/sliders', verbose_name='تصویر اسلایدر'),
        ),
    ]
