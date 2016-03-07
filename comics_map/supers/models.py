from __future__ import unicode_literals
import datetime
from django.db import models

class IRLCity(models.Model):
	name = models.CharField(max_length=150,default="default")
	province = models.CharField(max_length=150,default="default") #or state
	longitude = models.IntegerField(default=0)
	latitude = models.IntegerField(default=0)
	def __str__(self):
		return "{0} , {1}".format(self.name, self.province)
	
	def num_supers(self):
		count = 0
		city_supers = self.supers_related.all()

		for sup in city_supers:
			count = count + 1
		return count
	

class Universe(models.Model):
	company_name = models.CharField(max_length=300)
	origin_country = models.CharField(max_length=150) #Change the max since this initial
	#version will only use Japan and the US
	def __str__(self):
		return self.company_name

class Super(models.Model):
	name = models.CharField(max_length=300,unique=True)
	identity = models.CharField(max_length=300,default="identity")
	origin_city = models.CharField(max_length=150)
	# origin_state = models.CharField(max_length=150)
	irl_city = models.ForeignKey(IRLCity,related_name="supers_related") #check to make
	#sure that's the right style for a related name
	company_universe = models.ForeignKey(Universe,related_name="supers_related")

	def __str__(self):
		return self.supername

