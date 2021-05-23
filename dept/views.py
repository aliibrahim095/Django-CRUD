from dept.models import Student
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from dept import *
from dept.forms import *
# Create your views here.
def home(request): 
    return HttpResponse("<h1> This is Home Page </h1>")
def getStudent(request, std_id):
    stud = Student.objects.get(id=std_id)
    context = {"student":stud}
    return render(request,'dept/student.html',context)

def getAllStudents(request):
    students = Student.objects.all()
    context = {"allstudents":students}
    return render(request,'dept/students.html',context)

def addNewStd(request):
    std_form = StudentForm()
    if request.method== "POST":
        std_form  = StudentForm(request.POST)
        if std_form.is_valid():
            std_form.save()
            return HttpResponseRedirect('/dept/allstd')
    context = {"student_form": std_form}
    return render(request,'dept/addnewstd.html',context)
    

def editStd(request, std_id):
    std = Student.objects.get(id=std_id)
    std_form = StudentForm(instance=std)
    if request.method== "POST":
        std_form  = StudentForm(request.POST,instance=std)
        if std_form.is_valid():
            std_form.save()
            return HttpResponseRedirect('/dept/allstd')
    context = {"student_form": std_form}
    return render(request,'dept/addnewstd.html',context)

def deleteStd(request, std_id):
    std = Student.objects.get(id=std_id)
    std.delete()
    return HttpResponseRedirect('/dept/allstd')
