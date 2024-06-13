from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView

from planets.models import Facility, Hostname, Method, Planet


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = {
            **super().get_context_data(**kwargs),
            "years": range(1992, 2024),
            "methods": Method.objects.all(),
            "hostnames": Hostname.objects.all(),
            "facilities": Facility.objects.all()
        }
        return context


class SearchResultView(ListView):
    model = Planet
    template_name = "search_results.html"

    def get_queryset(self) -> QuerySet[Any]:
        base_filter = Q()
        if self.request.GET.get("year_of_discovery") is not None:
            base_filter &= Q(year_of_discovery=self.request.GET["year_of_discovery"])
        if self.request.GET.get("discovery_method") is not None:
            base_filter &= Q(discovery_method__name__iregex=self.request.GET["discovery_method"])
        if self.request.GET.get("hostname") is not None:
            base_filter &= Q(hostname__name__iregex=self.request.GET["hostname"])
        if self.request.GET.get("discovery_facility") is not None:
            base_filter &= Q(discovery_facility__name__iregex=self.request.GET["discovery_facility"])

        return Planet.objects.filter(base_filter)
