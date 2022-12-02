from django.db import models
from jalali_date import date2jalali


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت', null=True, blank=True)
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک', null=True, blank=True)
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class IntroduceSection(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    introduce_txt = models.TextField(max_length=20000, verbose_name='متن معرفی', blank=True)
    activities = models.TextField(max_length=2000, verbose_name='فعالیت ها', blank=True)
    image = models.ImageField(upload_to='images/blog', verbose_name='تصویر معرفی', null=True, blank=True)

    class Meta:
        verbose_name = 'اطلاعات شرکت'
        verbose_name_plural = 'اطلاعات شرکت'

    def __str__(self):
        return self.title


class Cooperating(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    text = models.TextField(max_length=20000, verbose_name='متن', blank=True)
    inviting_txt = models.TextField(max_length=20000, verbose_name='متن دعوت', blank=True)

    class Meta:
        verbose_name = 'معرفی'
        verbose_name_plural = 'معرفی'

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان', null=True, blank=True)
    subtitle = models.TextField(max_length=2000, verbose_name='زیر عنوان', null=True, blank=True)
    short_txt = models.TextField(max_length=2000, verbose_name='متن کوتاه', null=True, blank=True)
    service_title = models.CharField(max_length=200, verbose_name='عنوان خدمات')
    service_txt = models.TextField(max_length=2000, verbose_name='متن خدمات')
    image = models.ImageField(upload_to='images/services', verbose_name='تصویر معرفی', null=True, blank=True)
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک', null=True, blank=True)
    url = models.URLField(max_length=500, verbose_name='لینک', null=True, blank=True)

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return self.service_title


class TheBestActivities(models.Model):
    short_title = models.CharField(max_length=300, verbose_name='عنوان کوتاه')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن آکاردئون', null=True)

    class Meta:
        verbose_name = 'بهترین فعالیت ها'
        verbose_name_plural = 'بهترین فعالیت ها'

    def __str__(self):
        return self.title


class Managers(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام')
    post = models.CharField(max_length=300, verbose_name='سمت')
    about = models.CharField(max_length=300, verbose_name='درباره...')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    image = models.ImageField(upload_to='images/services', verbose_name='تصویر معرفی', null=True, blank=True)

    class Meta:
        verbose_name = 'مدیر'
        verbose_name_plural = 'مدیران'

    def __str__(self):
        return self.name


class RelatedCompanies(models.Model):
    image = models.ImageField(upload_to='images/companies-image', verbose_name='تصویر لوگو شرکت', null=True, blank=True)

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'


class Customers(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام')
    post = models.CharField(max_length=300, verbose_name='سمت')
    text = models.TextField(max_length=300, verbose_name='متن پیام')
    image = models.ImageField(upload_to='images/customers', verbose_name='تصویر', null=True, blank=True)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'

    def __str__(self):
        return self.name


class MDriver(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    text = models.TextField(max_length=20000, verbose_name='متن', blank=True)

    class Meta:
        verbose_name = 'MDriver'
        verbose_name_plural = 'MDriver'

    def __str__(self):
        return self.title