from django.conf.urls.defaults import *
from openissues import views

urlpatterns = patterns('',
	url(r'^create/$', views.create, name='openissue_create'),
	url(r'^all/$', views.all, name='openissues_all'),
)