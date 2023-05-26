from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . models import Students
from .forms import StudentForm
# Create your views here.


def test_django(request):
    return HttpResponse('<h1>Shri Ganesha<h1>')

def render_template1(request):
    return render(request, 'students/students.html')     

def dynamic_template2(request):
    students_dict = {
        'first_name': 'Hemant',
        'last_name' : 'Patil'
    }
    return render(request,'students/students.html',students_dict)

def datetimefilter(request):
    dt = datetime.now()
    time_dict = {
        'dt' :dt
    }

    return render(request,'students/students.html',time_dict)


def dashboardfunc(request):

    return render(request, 'students/dashboard.html')

# def subject(request)

def listOfStudents(request):
    studentList = {
        'names':['Hemant','Raj',"Utkarsh"]
    }

    return render(request,'students/students.html',studentList)


def getStudentData(request):
    stud = Students.objects.all()

    return render(request,'students/students.html',{'stu':stud} ) 


def specificData(request , id=None):
    if id is not None:
        stud = Students.objects.get(id=id)

    return render(request,'students/students.html',{'data':stud})


def addData(request):
    form = StudentForm()

    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            


    context = {'form': form}
    return render(request,'students/post.html',context)