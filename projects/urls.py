from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.home, name="home"),
    path("supervisors/", views.all_supervisors, name = "supervisor-list"),
    path("projects/index/", views.all_projects, name = "project-list"),
    path("projects/index/<int:id>/", views.project, name = "project"),
    path("projects/add_project/", views.add_project, name = "add-project"),
    path("projects/staff/edit/<int:id>/", views.edit_project, name = "edit-project"),
    path("projects/staff/index/", views.project_index, name = "project-index"),
    path("projects/search_projects/", views.search_projects, name = "search-projects"),
 ]
