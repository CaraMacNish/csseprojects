from django.shortcuts import render
from .models import Supervisor, Project

# Create your views here.

def all_supervisors(request):
    supervisor_list = Supervisor.objects.all()
    return render(request, "projects/supervisor_list.html", 
        {'supervisor_list': supervisor_list})

def project(request, id):
    proj = Project.objects.get(pk=id)
    return render(request, "projects/project.html", {"project": proj} )

def all_projects(request):
    project_list = Project.objects.all()
    eligible_list = []
    for project in project_list:
        eligible_list.append([project.honours, project.mds, project.engineering])    
    return render(request, "projects/project_list.html", 
        {'project_list': project_list, 'eligible_list': eligible_list})

def home(request):
    return render(request, "projects/home.html", {})
