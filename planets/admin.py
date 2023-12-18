from django.contrib import admin

from .models import Facility, Hostname, Method, Planet

admin.site.register((Method, Hostname, Facility, Planet))
