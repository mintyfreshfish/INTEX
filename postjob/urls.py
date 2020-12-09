from .views import addJobPageView, storeJobPageView, companyPageView, removeJobPageView, resultJobPageView
from .views import updateJobPageView, returnJobPageView, recommendApplicantPageView, azure_matchbox2
from django.urls import path

urlpatterns = [
    path("", companyPageView, name="company"),

    path("addjob/", addJobPageView, name="addjob"),
    path("storejob/", storeJobPageView, name="storejob"),

    path("removejob/", removeJobPageView, name="removejob"),
    path("resultjob/", resultJobPageView, name="resultjob"),

    path("updatejob/", updateJobPageView, name="updatejob"),
    path("returnjob/", returnJobPageView, name="returnjob"),

    path("recommend/", recommendApplicantPageView, name="recommender2"),
    path("azure/", azure_matchbox2, name="azure2"),
]