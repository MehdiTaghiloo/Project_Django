from django.urls import path, include
from . import views
import accounts

urlpatterns = [
    path('site/', views.main_page, name='main'),
    path('home/', views.home_page, name='home'),
    path('logout/', accounts.views.logout, name='logout'),
    path('python/', include('courses.urls')),
    path('django/', include('courses.urls')),
    path('requests/', include('courses.urls')),
]