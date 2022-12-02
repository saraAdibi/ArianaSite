from django.shortcuts import render

from django.views.generic.base import TemplateView

from site_module.models import SiteSetting, FooterLinkBox, Slider, IntroduceSection, Cooperating, Services, \
    TheBestActivities, Managers, RelatedCompanies, Customers, MDriver


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        introduce = IntroduceSection.objects.all()
        cooperate = Cooperating.objects.all()
        services = Services.objects.all()
        best_activities = TheBestActivities.objects.all()
        manager = Managers.objects.all()
        related_companies = RelatedCompanies.objects.all()
        customers = Customers.objects.all()
        context['sliders'] = sliders
        context['introduce'] = introduce
        context['cooperate'] = cooperate
        context['services'] = services
        context['best_activities'] = best_activities
        context['manager'] = manager
        context['related_companies'] = related_companies
        context['customers'] = customers
        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()

    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        mdriver = MDriver.objects.all()
        context['site_setting'] = site_setting
        context['mdriver'] = mdriver

        return context

#
# def activity(request):
#     activities = Activities.objects.filter(is_active=True)
#     context = {
#         'activities': activities
#     }
#     return render(request, 'home_module/activities.html', context)
