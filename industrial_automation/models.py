from django.db import models
# Create your models here.
from jalali_date import date2jalali


class IndustrialAutomation(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان آموزش')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='سرفصل های دوره', null=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'آموزش اتوماسیون صنعتی'
        verbose_name_plural = 'آموزش اتوماسیون صنعتی'


