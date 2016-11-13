from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^cities/$', views.cities),
	url(r'^cities/(?P<city_id>[0-9]+)/roliks/$', views.roliks, name='roliks'),
	url(r'^rolik/(?P<rolik_id>[0-9]+)/$', views.rolik, name='rolik'),
	url(r'^cities/(?P<city_id>[0-9]+)/objects/$', views.objects, name='objects'),
	url(r'^object/(?P<object_id>[0-9]+)/$', views.object, name='object'),
]