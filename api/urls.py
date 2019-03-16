from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('post/organisation/', views.post_organisation, name='post_organisation'),
    path('get/organisation/', views.get_organisation, name='get_organisation'),
    path('post/student/', views.post_student, name='post_student'),
    path('get/student/', views.get_student, name='get_student'),
    path('get/scholarship/', views.get_scholarship, name='get_scholarship'),
    path('get/type/', views.get_type, name='get_type'),
    path('get/scholarship/eligible/', views.get_scholarship_eligible, name='get_scholarship_eligible'),
]
