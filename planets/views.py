from typing import Any

from django.views.generic import TemplateView

from planets.models import Facility, Hostname, Method


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
