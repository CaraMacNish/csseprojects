from django.contrib import admin

# Register your models here.
from .models import Supervisor
from .models import Project

admin.site.register(Supervisor)
admin.site.register(Project)

