from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import date
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

def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.instance.current_date = date.today().isoformat()
        form.save()
        return redirect('project', project.pk)

    return render(request, "projects/edit_project.html", {"project": project, 'form': form })

def all_supervisors(request):
    supervisor_list = Supervisor.objects.all().order_by('lastname')
    return render(request, "projects/supervisor_list.html", 
        {'supervisor_list': supervisor_list})

def project(request, id):
    proj = Project.objects.get(pk=id)
    return render(request, "projects/project.html", {"project": proj} )

def all_projects(request):
    project_list = Project.objects.all().exclude(visible=False).order_by('-current_date')
    eligible_list = []
    for project in project_list:
        eligible_list.append([project.honours, project.mds, project.engineering])    
    return render(request, "projects/project_list.html", 
        {'project_list': project_list, 'eligible_list': eligible_list})

def project_index(request):
    project_list = Project.objects.all().order_by('primary__lastname')
    return render(request, "projects/project_index.html", 
        {'project_list': project_list})
        
def search_projects(request):
    if request.method == "POST":
        searched = request.POST['searched']

        project_list = Project.objects.all().exclude(visible=False).filter(
            Q(primary__lastname__contains = searched) |
            Q(primary__firstname__contains = searched) |
            Q(cosupervisor__lastname__contains = searched) |
            Q(cosupervisor__firstname__contains = searched) |
            Q(external__contains = searched) |
            Q(title__contains = searched) |
            Q(description__contains = searched)
        ).order_by('-current_date')
        return render(request, "projects/search_projects.html", 
            {'searched': searched, 'project_list': project_list})
    else:
        project_list = Project.objects.all().order_by('-current_date')
        return render(request, "projects/search_projects.html", 
            {'project_list': project_list})

def home(request):
    return render(request, "projects/home.html", {})
