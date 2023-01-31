from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Supervisor, Project
from .forms import ProjectForm

# Create your views here.

def add_project(request):
    submitted = False
 #   error = False
 #   supervisor_list = Supervisor.objects.all()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
#        
#        return HttpResponseRedirect('?error=True')
    else:
        form = ProjectForm()
 #       supervisor_list = Supervisor.objects.all()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "projects/add_project.html", {'form': form, 'submitted': submitted})

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
