from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test_django(request):
    return HttpResponse('<h1>Shri Ganesha<h1>')

def render_template1(request):
    return render(request, 'students.html')     

def dynamic_template2(request):
    students_dict = {
        'first_name': 'Hemant',
        'last_name' : 'Patil'
    }
    return render(request,'students.html',students_dict)
