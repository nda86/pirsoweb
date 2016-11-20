from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^cities/$', views.cities),
	url(r'^cities/(?P<city_id>[0-9]+)/roliks/$', views.roliks, name='roliks'),
	url(r'^admin/rekl/rolik/(?P<rolik_id>[0-9]+)/change/$', views.rolik, name='rolik'),
	url(r'^cities/(?P<city_id>[0-9]+)/objects/$', views.objects, name='objects'),
	url(r'^admin/rekl/object/(?P<object_id>[0-9]+)/change/$', views.object, name='object'),
	url(r'^objects/$', views.objects_all, name='objects_all'),
	url(r'^roliks/$', views.roliks_all, name='roliks_all'),
]


# /admin/rekl/object/3/change/
# /admin/rekl/rolik/1/change/