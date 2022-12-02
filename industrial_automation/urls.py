from django.urls import path
from . import views

urlpatterns = [
    path('', views.Industrial_Automation.as_view(), name='AutomationTraining'),
]
