from django.shortcuts import render, redirect

# Create your views here.
from crudApp.forms import EmployeeForm

# index as empty on first hit and in second hit it will store data in the model
from crudApp.models import Emp


def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form=EmployeeForm()
    return render(request,"crudApp/index.html",{"form":form})

# to show all elements
def show(request):
    employees=Emp.objects.all()
    return render(request,"crudApp/show.html",{"employees":employees})
# to edit details
def edit(request,id):
    employee=Emp.objects.get(id=id)
    return render(request,"crudApp/edit.html", {'employee':employee})
# update
def update(request, id):
    employee = Emp.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'crudApp/edit.html', {'employee': employee})

def destroy(request, id):
    employee = Emp.objects.get(id=id)
    employee.delete()
    return redirect("/show")