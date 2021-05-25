from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

import datetime


from datetime import date, timedelta

import django_filters
# Create your views here.


ll=[]
def returnA():

    for i in Employee.objects.filter(datetimeC__gt=(date.today() - timedelta(days=2)), datetimeC__lte= datetime.datetime.now()).all():
        
        ll.append({"lattitude:",i.lattitude,"longtitude:",i.longtitude,"vehicle:",i.vehicle,"datetime:",i.datetimeC})
        print(["lattitude:",i.lattitude,"longtitude:",i.longtitude,"vehicle:",i.vehicle,"datetime:",i.datetimeC])
    print(ll)
    #return ll
    print(Employee.objects.filter(datetimeC__gt=(date.today() - timedelta(days=2)), datetimeC__lte= datetime.datetime.now()).all())
    return Employee.objects.filter(datetimeC__gt=(date.today() - timedelta(days=2)), datetimeC__lte= datetime.datetime.now()).all()


def employee_list(request):
    context = {'employee_list':returnA() }
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
