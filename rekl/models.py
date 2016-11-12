from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	name = models.CharField(max_length=50, unique=True)
	def __str__(self):
		return str(self.name)

class Rolik(models.Model):
	# BRATSK = 'BRT'
	# KRASNOYARSK = 'KRS'
	# IRKUTSK = 'IRK'
	# STAVROPOL = 'SVP'
	# COMMON = 'CMN'
	# OTHER = 'OTH'
	# CITY_CHOICE = (
	# 	(BRATSK, 'Bratsk'),
	# 	(KRASNOYARSK, 'Krasnoyarsk'),
	# 	(IRKUTSK, 'Irkutsk'),
	# 	(STAVROPOL, 'Stavropol'),
	# 	(COMMON, 'Common'),
	# 	(OTHER, 'Other'),
	# )
	title = models.CharField(max_length=20, unique=True)
	title2 = models.CharField(max_length=40, unique=True)
	duration = models.IntegerField()
	active = models.BooleanField(default=True)
	city = models.ForeignKey('City',on_delete=models.CASCADE, null=True)
	comment=models.CharField(max_length=200, default="")
	date_creation = models.DateTimeField(auto_now_add=True, editable=False)
	date_modify = models.DateTimeField(auto_now=True, editable=False)
	def __str__(self):
		return str(self.title + ' - ' + self.title2)

