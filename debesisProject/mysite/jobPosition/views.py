from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from workers.models import JobPosition
from .forms import JobPositionForm


def jobPositonList(request):
    queryset = JobPosition.objects.all()
    context = {
        "obj_list": queryset,
        "title": "Job positions",
    }
    return render(request, 'jobPosition/index.html', context)


def createJobPosition(request):
    form = JobPositionForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'jobPosition/jobPosition_form.html', context)


def editJobPosition(request, id=None):
    instance = get_object_or_404(JobPosition, id=id)
    form = JobPositionForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.name,
        "form": form,
        "instance": instance,
    }
    return render(request, 'jobPosition/jobPosition_form.html', context)

def jobPositionDetails(request, id=None):
    instance = get_object_or_404(JobPosition, id=id)
    context = {
        'instance': instance,
        'title': "details",
    }
    return render(request, 'jobPosition/details.html', context)

def deleteJobPosition(request, id=None):
    instance = get_object_or_404(JobPosition, id=id)
    instance.delete()
    return redirect('jobPosition:job_list')








