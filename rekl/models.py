from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return str(self.name)

class Rolik(models.Model):
	title = models.CharField(max_length=20, unique=True)
	title2 = models.CharField(max_length=40, unique=True)
	duration = models.IntegerField()
	active = models.BooleanField(default=True)
	city = models.ForeignKey('City',on_delete=models.CASCADE, null=True)
	comment=models.CharField(max_length=200, default="-")
	date_creation = models.DateTimeField(auto_now_add=True, editable=False)
	date_modify = models.DateTimeField(auto_now=True, editable=False)
	def __str__(self):
		return str(self.title + ' - ' + self.title2)

class Object(models.Model):
	pi_address = models.CharField(max_length=100, unique=True)
	pi_id = models.CharField(max_length=10, unique=True)
	pi_ip = models.GenericIPAddressField(protocol='IPv4', default='0.0.0.0')
	pi_alsa = models.IntegerField(default=0)
	pi_mpc = models.IntegerField(default=0) 
	pi_mpg = models.IntegerField(default=0) 
	pi_tel = models.CharField(max_length=50, default="-")
	pi_comment = models.CharField(max_length=200, default="-")
	pi_roliks = models.ManyToManyField('Rolik')
	active = models.BooleanField(default=True)
	city = models.ForeignKey('City',on_delete=models.CASCADE, null=True)
	date_modify = models.DateTimeField(auto_now=True, editable=False)
	date_creation = models.DateTimeField(auto_now_add=True, editable=False)
	def __str__(self):
		address = u' '.join(self.pi_address).encode('utf-8').strip()
		return str(self.pi_id + ' - ' + self.pi_ip + ' - ' + address)