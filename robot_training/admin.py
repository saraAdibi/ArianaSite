from django.contrib import admin
from . import models


# Register your models here.
class RobotAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']



admin.site.register(models.Robot, RobotAdmin)
admin.site.register(models.RobotReadMore)
