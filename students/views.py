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

    print(dir(request))
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            


    context = {'form': form}
    return render(request,'students/post.html',context)


# ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__deepcopy__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#  '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_body', 
# '_current_scheme_host', '_encoding', '_files', '_get_full_path', '_get_post', 
# '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', 
# '_mark_post_parse_error', '_messages', '_post', '_read_started', 
# '_set_content_type_params', '_set_post', '_stream', '_upload_handlers',
#  'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 
# 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 
# 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 
# 'get_signed_cookie', 'headers', 'is_secure', 'meta_non_picklable_attrs', 
# 'method', 'non_picklable_attrs', 'parse_file_upload', 'path', 'path_info', 
# 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 
# 'upload_handlers', 'user']      
# <QueryDict: {'csrfmiddlewaretoken': ['eFldUiOdw30Mbft89FZOSCDMxibJwDZNCx6xGY5ICqfGIK75NNTCOX6xfYTLLsON'],