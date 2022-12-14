# Generated by Django 3.1.4 on 2022-11-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0024_relatedcompanies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام')),
                ('post', models.CharField(max_length=300, verbose_name='سمت')),
                ('text', models.TextField(max_length=300, verbose_name='متن پیام')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/customers', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتری ها',
            },
        ),
    ]
