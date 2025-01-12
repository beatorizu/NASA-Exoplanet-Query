from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.SearchResultView.as_view(), name="search_planets"),
    path("", views.HomePageView.as_view(), name="home"),
]
