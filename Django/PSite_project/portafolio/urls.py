from django.conf.urls import patterns, url
from portafolio import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^courses/$',views.courses,name='courses'),
	url(r'^jobs/$',views.jobs,name='jobs'),
	)