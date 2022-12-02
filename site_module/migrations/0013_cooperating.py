# Generated by Django 3.1.4 on 2022-10-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0012_introducesection_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('text', models.TextField(blank=True, max_length=20000, verbose_name='متن')),
                ('inviting_txt', models.TextField(blank=True, max_length=20000, verbose_name='متن دعوت')),
            ],
        ),
    ]
