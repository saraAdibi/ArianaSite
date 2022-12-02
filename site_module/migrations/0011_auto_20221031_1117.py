# Generated by Django 3.1.4 on 2022-10-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0010_auto_20221031_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='introducesection',
            name='activities',
            field=models.TextField(blank=True, max_length=2000, verbose_name='فعالیت ها'),
        ),
        migrations.AddField(
            model_name='introducesection',
            name='introduce_txt',
            field=models.TextField(blank=True, max_length=20000, verbose_name='متن معرفی'),
        ),
    ]