from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^roliks/$', views.roliks),
	url(r'^roliks/(?P<rolik_id>[0-9]+)/$', views.rolik, name='rolik'),
]