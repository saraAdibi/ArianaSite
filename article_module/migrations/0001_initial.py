# Generated by Django 3.1.4 on 2022-10-27 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('url_title', models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی مقاله',
                'verbose_name_plural': 'دسته بندی های مقاله',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, verbose_name='عنوان در url')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('text', models.TextField(verbose_name='متن مقاله')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('selected_categories', models.ManyToManyField(to='article_module.ArticleCategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
