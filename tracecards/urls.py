from django.conf.urls.defaults import *
from tracecards import views

urlpatterns = patterns('',
	url(r'^create/$', views.create, name='tracecard_create'),
	url(r'^all/$', views.all, name='tracecards_all'),
)