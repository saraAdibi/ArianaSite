from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from industrial_automation.models import IndustrialAutomation


# Create your views here.

class Industrial_Automation(ListView):
    model = IndustrialAutomation
    paginate_by = 20
    template_name = 'article_module/automaion_training.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Industrial_Automation, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(Industrial_Automation, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query

