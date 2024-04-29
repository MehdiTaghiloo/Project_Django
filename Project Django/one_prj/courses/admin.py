from django.contrib import admin
from .models import PythonCourse, DjangoCourse, RequestsCourse

# Register your models here.

admin.site.register(PythonCourse)
admin.site.register(DjangoCourse)
admin.site.register(RequestsCourse)
