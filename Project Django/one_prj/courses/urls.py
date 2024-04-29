from django.urls import path
from . import views

urlpatterns = [
    path('python/', views.pythoncourse, name='pythoncourse'),
    path('django/', views.djangocourse, name='djangocourse'),
    path('requests/', views.requestscourse, name='requestscourse'),
]

