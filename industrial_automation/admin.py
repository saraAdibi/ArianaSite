from django.contrib import admin
from . import models


# Register your models here.
class AutomationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']


admin.site.register(models.IndustrialAutomation, AutomationAdmin)


