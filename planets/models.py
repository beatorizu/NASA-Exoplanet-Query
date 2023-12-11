from django.db import models

class Planet(models.Model):
	year_of_discovery = models.IntegerField()
	discovery_method = models.CharField(max_length=30)
	hostname = models.CharField(max_length=30)
	discovery_facility = models.CharField(max_length=30)
