from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('post/organisation/', views.post_organisation, name='post_organisation'),
]
