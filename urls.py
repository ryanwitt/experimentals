from django.conf.urls.defaults import *
import experimentals_generator.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^experimentals/', include('experimentals_generator.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)
