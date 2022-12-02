from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from robot_training.models import Robot, RobotReadMore


# Create your views here.

class RobotTraining(ListView):
    model = Robot
    paginate_by = 4
    template_name = 'article_module/robot_training.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RobotTraining, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(RobotTraining, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class RobotRead(ListView):
    model = RobotReadMore
    paginate_by = 4
    template_name = 'article_module/RobotReadMore.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RobotRead, self).get_context_data(*args, **kwargs)
        return context


