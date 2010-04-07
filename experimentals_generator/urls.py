from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^(?P<id>\d+)/', views.experimental),
)
