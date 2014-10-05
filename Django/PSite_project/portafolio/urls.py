from django.conf.urls import patterns, url
from portafolio import views

urlpatterns = patterns('', 
				url(r'^$',views.index,name='index'),)