from __future__ import unicode_literals

from django.db import models

class Rolik(models.Model):
	title = models.CharField(max_length=20, unique=True)
	title2 = models.CharField(max_length=40, unique=True)
	duration = models.IntegerField()
	date_creation = models.DateTimeField(auto_now_add=True, editable=False)
	date_modify = models.DateTimeField(auto_now=True, editable=False)

