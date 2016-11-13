from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rolik, City, Object



def index(request):
	return render(request, "rekl/index.html")



def cities(request):
	city_list = City.objects.all()
	context = {
		'city_list': city_list,
		'title': 'List of City',
	}
	return render(request, "rekl/cities.html", context)



# roliks################################################################
def roliks(request, city_id):
	rolik_list = Rolik.objects.filter(city_id=city_id)
	context = {
		'rolik_list': rolik_list,
		'title': 'List of Roliks',
		'caption': City.objects.get(pk=city_id)
	}
	return render(request, "rekl/roliks.html", context)

def rolik(request, rolik_id):
	rolik = Rolik.objects.get(pk=rolik_id)
	context = {
		'rolik': rolik,
		'title': 'Detail Rolik'
	}
	return render(request, "rekl/rolik.html", context)
#########################################################################






# objects################################################################
def objects(request, city_id):
	object_list = Object.objects.filter(city_id=city_id)
	context = {
		'object_list': object_list,
		'title': 'List of Objects',
		'caption': City.objects.get(pk=city_id)
	}
	return render(request, "rekl/objects.html", context)


def object(request, object_id):
	pi_object = Object.objects.get(pk=object_id)
	context = {
		'object': pi_object,
		'title': 'Detail Object'
	}
	return render(request, "rekl/object.html", context)

#########################################################################





