from django.db import models

class Method(models.Model):
	name = models.CharField(unique=True, max_length=30)


class Hostname(models.Model):
	name = models.CharField(unique=True, max_length=30)


class Facility(models.Model):
	name = models.CharField(unique=True, max_length=30)

	class Meta:
		verbose_name_plural = "Facilities"


class Planet(models.Model):
	year_of_discovery = models.IntegerField()
	discovery_method = models.ForeignKey(Method, on_delete=models.CASCADE, null=True, to_field="name")
	hostname = models.ForeignKey(Hostname, on_delete=models.CASCADE, null=True, to_field="name")
	discovery_facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, to_field="name")

	search_fields = ["discovery_method__name", "hostname__name", "discovery_facility__name"]
