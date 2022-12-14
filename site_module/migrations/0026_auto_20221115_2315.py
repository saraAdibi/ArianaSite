# Generated by Django 3.1.4 on 2022-11-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0025_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='MDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, max_length=20000, verbose_name='متن')),
                ('mdriver_text', models.TextField(blank=True, max_length=20000, verbose_name='متن mdriver')),
            ],
            options={
                'verbose_name': 'MDriver',
                'verbose_name_plural': 'MDriver',
            },
        ),
        migrations.AlterModelOptions(
            name='cooperating',
            options={'verbose_name': 'معرفی', 'verbose_name_plural': 'معرفی'},
        ),
        migrations.AlterModelOptions(
            name='introducesection',
            options={'verbose_name': 'اطلاعات شرکت', 'verbose_name_plural': 'اطلاعات شرکت'},
        ),
    ]
