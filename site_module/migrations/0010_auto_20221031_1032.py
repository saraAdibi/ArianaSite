# Generated by Django 3.1.4 on 2022-10-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0009_delete_bestfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroduceSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'معرفی شرکت',
                'verbose_name_plural': 'معرفی شرکت',
            },
        ),
        migrations.DeleteModel(
            name='Introducing',
        ),
    ]
