from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


admin.site.register(models.SiteSetting)
admin.site.register(models.IntroduceSection)
admin.site.register(models.TheBestActivities)
admin.site.register(models.Managers)
admin.site.register(models.Customers)
admin.site.register(models.MDriver)
admin.site.register(models.RelatedCompanies)
admin.site.register(models.Cooperating)
admin.site.register(models.Services)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.FooterLink, FooterLinkAdmin)
