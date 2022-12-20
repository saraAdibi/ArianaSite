"""eshop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from django.contrib.sitemaps.views import sitemap
from django.views.static import serve

urlpatterns = [
    # debug = false
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^STATIC/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('', include('home_module.urls'), name='homemodule'),
    path('', include('account_module.urls')),
    path('articles/', include('article_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('robot-training/', include('robot_training.urls')),
    path('software_training/', include('software_training.urls')),
    path('automation-training/', include('industrial_automation.urls')),
    path('products/', include('product_module.urls')),
    path('projects/', include('ariana_projects.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
