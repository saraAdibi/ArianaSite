from django.urls import path
from . import views

urlpatterns = [
    path('', views.Software_training.as_view(), name='SoftwareTraining'),
]
