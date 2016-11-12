from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rolik



def index(request):
	return render(request, "rekl/index.html")

def roliks(request):
	rolik_list = Rolik.objects.all()
	context = {
		'rolik_list': rolik_list,
		'title': 'List of Roliks'
	}
	return render(request, "rekl/roliks.html", context)

def rolik(request, rolik_id):
	rolik = Rolik.objects.get(pk=rolik_id)
	context = {
		'rolik': rolik,
		'title': 'Detail Rolik'
	}
	return render(request, "rekl/rolik.html", context)






