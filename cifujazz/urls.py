from django.conf.urls import include, url
from django.contrib import admin

from cifujazz.apps.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
