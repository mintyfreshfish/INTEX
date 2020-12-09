from .views import findJobPageView, searchJobPageView, employeePageView, recommendJobPageView, azure_matchbox
from django.urls import path

urlpatterns = [
    path("", employeePageView, name="employee"),

    path("recommend/", recommendJobPageView, name="recommender"),
    path("azure/", azure_matchbox, name="azure"),

    path("search/", findJobPageView, name="findjobs"),
    path("findjob/", searchJobPageView, name="jobs"),
]