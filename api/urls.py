from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('post/organisation/', views.post_organisation, name='post_organisation'),
    path('get/organisation/<str:uid>', views.get_organisation, name='get_organisation'),
    path('post/student/', views.post_student, name='post_student'),
    path('get/student/<str:uid>', views.get_student, name='get_student'),
]
