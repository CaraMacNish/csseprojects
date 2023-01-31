from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.home, name="home"),
    path("supervisors/", views.all_supervisors, name = "supervisor-list"),
    path("projects/index/", views.all_projects, name = "project-list"),
    path("projects/index/<int:id>/", views.project, name = "project"),
    path("projects/add_project/", views.add_project, name = "add-project"),
    ]
