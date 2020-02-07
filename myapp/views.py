from django.shortcuts import render,redirect
from myapp.forms import *
from myapp.models import * 

# def add(request):
#     if request.method == "POST":
#         stu = Employee(request.POST)
#         if stu.is_valid():
#             stu.save()
#             return redirect('/')
#         else:
#             stu = Employee()
#             return render(request,'index.html',{'stu':stu})

def search(request):
    stu = Employee(request.POST)
    if request.method == "POST":
        name = request.POST['fname']
        num = student.objects.all(fname = name)
    else:
        stu = Employee()
    return render(request,'search.html',{'stu':stu})

def remove(request):
    if request.method == "POST":
        name = request.POST['fname']
        num = student.objects.all(fname = name)
        num.delete()
        return redirect("/delete")
    else:
        stu=Employee()
        return render(request,'delete.html',{'stu':stu})

def add1(request):
    if request.method == "POST":
        stu = Employee(request.POST)
        if stu.is_valid():
            stu.save()
            return redirect('/')
    else:
        stu= Employee()
    return render(request,'index.html',{'stu':stu})