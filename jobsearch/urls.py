from .views import findJobPageView, searchJobPageView
from django.urls import path

urlpatterns = [
    path("", findJobPageView, name="findjobs"),
    path("findjob/", searchJobPageView, name="jobs"),
]