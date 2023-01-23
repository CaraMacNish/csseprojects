from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("supervisors/", views.all_supervisors, name = "supervisor-list"),
    path("projects/", views.all_projects, name = "project-list"),
    path("projects/<int:id>/", views.project, name = "project"),
    ]
