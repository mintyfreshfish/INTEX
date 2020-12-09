from django.shortcuts import render
from homepages.models import JobListing
from homepages.models import JobOrganization
from django.http import HttpResponse

def employeePageView(request):
    return render(request, 'jobsearch/companyPage.html')


def recommendJobPageView(request):
    return render(request, 'jobsearch/recommendJobs.html')

def numToName(number):
    company_name = {
        "thisThing": JobOrganization.objects.filter(pk = number).first()
        } 
        
    return company_name
    


def azure_matchbox(request):
    from urllib import request as r
    import json 

    data =  {
            "Inputs": {
              "input1": {
                "ColumnNames": ["user_id", "organization_id"],
                "Values": [[ 
                  request.GET['company_id'], 
                  request.GET['user_id'], 
                  ]]
               }
              }
            }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/da57264d91d949eb8dad2a2f8b45a083/services/24b0ea7090b34529a82e5522aafeb6b4/execute?api-version=2.0&details=true'
    api_key = 'neLYaW0VUosZmrm0NwzFhQ9cRh0j1E1ty3Ns7Lt17CEFh+bLwh597o1sF0M4dkCYk3JsouErVD/2rWyNl+u/tg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = r.Request(url, body, headers) 
    response = r.urlopen(req)
    result = response.read()
    result = json.loads(result)

    prediction = result['Results']['output1']['value']['Values'][0]
    data = {'matchbox_results':str(f'1. {prediction[0]}, 2. {prediction[1]}, 3. {prediction[2]}, 4. {prediction[3]}, 5. {prediction[4]} ')}
    
    thisThing = JobOrganization.objects.filter(pk = prediction[1]).first()
    
    Beans = {
        "name" : JobOrganization.objects.filter(pk = prediction[1]).first(),
        "num" : prediction[0]
    }
    
    return render(request, 'jobsearch/recommendJobs.html', Beans)


def findJobPageView(request) :
    data = JobListing.objects.all()
    context = {
        "job_list": data
    }
    return render(request, 'jobsearch/searchJobs.html', context)


def searchJobPageView(request) :
    sjobName = request.GET.get('job_title')
    sCity = request.GET.get('city')
    data = JobListing.objects.filter(job_title=sjobName, city=sCity) 

    
    r = list(JobListing.objects.filter(organization__id="5").all())
    print(r)
    print(data)
    beans = []
    
    for l in range(len(r)):
        beans.append(str(r[l]).replace("*", " in "))

    if data.count() > 0:
        context = {
            "job_list" : data,
            "loop" : beans
        }
        return render(request, 'jobsearch/displayJobs.html', context)
    else:
        return HttpResponse("Not found")
    
    
    