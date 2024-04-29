from django.shortcuts import render, redirect
from .models import PythonCourse, DjangoCourse, RequestsCourse

# Create your views here.

def pythoncourse(request):
    video_1 = PythonCourse.objects.all()
    return render(request, 'python_course.html', {'video_1' : video_1})
    

# ------------------------------------------------------------ #

def djangocourse(request):
    video_2 = DjangoCourse.objects.all()
    return render(request, 'django_course.html', {'video_2' : video_2})

# ------------------------------------------------------------ #

def requestscourse(request):
    video_3 = RequestsCourse.objects.all()
    return render(request, 'requests_course.html', {'video_3' : video_3})


