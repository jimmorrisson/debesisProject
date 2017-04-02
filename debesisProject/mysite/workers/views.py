from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import JobPosition, Employee
from .forms import EmployeeForm
from django.contrib import messages


def emp_list(request):
    queryset = Employee.objects.all()
    context = {
        "object_list": queryset,
        "title": "My user list",
    }
    return render(request, 'workers/index.html', context)


def emp_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'workers/emp_form.html', context)


def emp_details(request, id=None):
    # instance = Post.objects.get(id=0)
    instance = get_object_or_404(Employee, id=id)
    context = {
        "first_name": instance.first_name,
        "instance": instance,
    }
    return render(request, 'workers/emp_detail.html', context)


def emp_update(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.first_name,
        "instance": instance,
        "form": form,
    }
    return render(request, 'workers/emp_form.html', context)


def emp_delete(request, id=None):
    instance = get_object_or_404(Employee, id=id)
    instance.delete()
    # essages.SUCCESS(request, "Successfully deleted")
    return redirect("workers:list")
