from django.urls import path
from . import views

urlpatterns = [
    path('', views.RobotTraining.as_view(), name='RobotTraining'),
    path('robot-read-more/', views.RobotRead.as_view(), name='RobotRead'),
]
