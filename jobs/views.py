from django.shortcuts import render
from .models import Job

# Create your views here.

def index(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html',  {'jobs':jobs})

def kevin(request):
    return render(request, 'jobs/kevin.html')