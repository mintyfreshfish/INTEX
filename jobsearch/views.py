from django.shortcuts import render
from .models import JobListing
from django.http import HttpResponse

def findJobPageView(request) :
    data = JobListing.objects.all()
    context = {
        "job_list": data
    }
    return render(request, 'jobsearch/searchJobs.html', context)

def searchJobPageView(request) :
    sjobName = request.GET.get('job_title')
    sCity = request.GET.get('city')
    data = JobListing.objects.get(job_title=sjobName, city=sCity)    

    if data.count() > 0:
        context = {
            "job_list" : data
        }
        return render(request, 'jobsearch/displayJobs.html', context)
    else:
        return HttpResponse("Not found")