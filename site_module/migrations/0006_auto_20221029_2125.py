# Generated by Django 3.1.4 on 2022-10-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_auto_20221029_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='about_us_text',
            field=models.TextField(blank=True, null=True, verbose_name='متن درباره ما سایت'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='site_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام سایت'),
        ),
    ]
