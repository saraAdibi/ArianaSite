# Generated by Django 3.1.4 on 2022-11-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0022_auto_20221101_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('post', models.CharField(max_length=300, verbose_name='سمت')),
                ('about', models.CharField(max_length=300, verbose_name='درباره...')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/services', verbose_name='تصویر معرفی')),
            ],
            options={
                'verbose_name': 'مدیر',
                'verbose_name_plural': 'مدیران',
            },
        ),
    ]
