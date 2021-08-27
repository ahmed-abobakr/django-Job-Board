from django.shortcuts import render

# Create your views here.

from .models import Job

def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs':job_list}
    return render(request, "job/job_list.htm", context)


def job_details(request, id):
    job = Job.objects.get(id=id)
    context = {'job':job}
    return render(request, "job/job_detail.htm", context)