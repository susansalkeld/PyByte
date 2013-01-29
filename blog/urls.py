from __future__ import absolute_import
from django.conf.urls.defaults import patterns, include, url
from . import views
from blog.models import Entry
from django.views.generic import list_detail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybyte.views.home', name='home'),
    # url(r'^pybyte/', include('pybyte.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^/?$', views.index),
    (r'^entry/(?P<entry_id>\d+)/$', views.entry),

)
