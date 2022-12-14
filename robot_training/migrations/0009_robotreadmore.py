# Generated by Django 3.1.4 on 2022-11-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot_training', '0008_auto_20221117_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotReadMore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان آموزش')),
                ('text', models.TextField(verbose_name='متن آموزش')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
            ],
            options={
                'verbose_name': 'آموزش ربات',
                'verbose_name_plural': 'آموزش ربات',
            },
        ),
    ]
