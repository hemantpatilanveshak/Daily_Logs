from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test_django),
    path('student/',views.render_template1),
    path('dynamic/',views.dynamic_template2),
]