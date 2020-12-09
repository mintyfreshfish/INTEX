from django.shortcuts import render

# Create your views here.

def indexPageView(request) :
    return render(request, 'homepages/index.html')

def aboutPageView(request) :
    return render(request, 'homepages/about.html')