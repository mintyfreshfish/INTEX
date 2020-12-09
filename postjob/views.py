from django.shortcuts import render
from django.http import HttpResponse
from homepages.models import JobListing, JobOrganization

# Company Home Page
def companyPageView(request) :
    return render(request, 'postjob/companyPage.html')


# Add Job Listing
def addJobPageView(request) :
    data = JobListing.objects.all()
    context = {
        "job_listings": data
    }
    return render(request, 'postjob/addJobPosts.html', context)

def storeJobPageView(request) :
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new JobListing object from the model (like a new record)
        new_job = JobListing()

        #Create new JobOrganization to make the job listing
        company_name = request.POST.get('company_name')
        company_email = request.POST.get('email')
        company_phone = request.POST.get('phone')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        size = request.POST.get('size')
        sector = request.POST.get('sector')

        organization = JobOrganization(company_name=company_name, company_email=company_email, company_phone=company_phone, street_address=street_address, city=city, state=state, zip=zip, size= size, sector=sector)
        organization.save()
        new_job.organization = organization

        new_job.job_title = request.POST.get('job_title')
        new_job.city = request.POST.get('city')
        new_job.contracts = request.POST.get('contracts')
        new_job.description = request.POST.get('description')

        #Save the job record
        new_job.save()
    
    data = JobListing.objects.all()
    context = {
        "job_listings" : data
    }
    return render(request, 'postjob/displayAddedJobs.html', context)  


# Delete Job Listing
def removeJobPageView(request) :
    data = JobListing.objects.all()

    context = {
        "job_listings": data
    }
    return render(request, 'postjob/removeJobs.html', context)

def resultJobPageView(request) :
    job = JobListing.objects.filter(job_title=request.GET['job_title'], city=request.GET['city'])
     
    data = JobListing.objects.all()

    if job.count() > 0:
        JobListing.objects.filter(job_title=request.GET['job_title'], city=request.GET['city']).delete() 
        context = {
            "job_listings" : data
        }
        return render(request, 'postjob/displayRemovedJobs.html', context)  
    else:
        return HttpResponse("Not found")



#Update Job Listing
def updateJobPageView(request) :
    data = JobListing.objects.all()
    context = {
        "job_listings": data
    }
    return render(request, 'postjob/updateJobListing.html', context)

def returnJobPageView(request) :
    job_title = request.GET['job_title']
    city = request.GET['city']
    sNewDescription = request.GET['new_description']

    #Find the job record
    job = JobListing.objects.filter(job_title=job_title, city=city) 
    
    if job.count() > 0:
        for  obj in job:
            obj.description = sNewDescription
            obj.save()         
        
        data = JobListing.objects.all()
        context = {
            "job_listings" : data
        }
        return render(request, 'postjob/returnJobPage.html', context)  
    
    else:
        return HttpResponse("Not found")


def recommendApplicantPageView(request):
    return render(request, 'postjob/recommendApplicants.html')


def azure_matchbox2(request):
    from urllib import request as r
    import json 

    data =  {
            "Inputs": {
              "input1": {
                "ColumnNames": ["organization_id", "user_id"],
                "Values": [[ 
                  request.GET['user_id'], 
                  request.GET['company_id'], 
                  ]]
               }
              }
            }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/da57264d91d949eb8dad2a2f8b45a083/services/fbef683987f64991934f9debf2a76a7b/execute?api-version=2.0&details=true'
    api_key = 'qcsdu9oEmUDu0JS2pekhMbRa0TFmac4bzXkuTGeiXW3Ydd333XU3PrvChmK+qV1hVPMuIM6gE/E8szKkFRZVhQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = r.Request(url, body, headers) 
    response = r.urlopen(req)
    result = response.read()
    result = json.loads(result)

    prediction = result['Results']['output1']['value']['Values'][0]
    data = {'matchbox_results2':str(f'1. {prediction[0]}, 2.{prediction[1]}, 3.{prediction[2]}, 4.{prediction[3]}, 5.{prediction[4]} ')}

    return render(request, 'postjob/recommendApplicants.html', data)
