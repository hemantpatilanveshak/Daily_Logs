from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test_django),
    path('student/',views.render_template1),
    path('dynamic/',views.dynamic_template2),
    path('datetime/',views.datetimefilter),
    path('dashboard/',views.dashboardfunc),
    path('studentlist/',views.listOfStudents),
    path('get/',views.getStudentData),
    path('get/<int:id>',views.specificData),
    path('post/',views.addData),
]