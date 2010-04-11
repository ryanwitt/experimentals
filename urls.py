from django.conf.urls.defaults import *
import experimentals_generator.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^experimentals/', include('experimentals_generator.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'', include(admin.site.urls)),
)
