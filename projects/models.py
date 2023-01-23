from django.db import models
from datetime import date

# Create your models here.

class Supervisor(models.Model):
    firstname = models.CharField("First name", max_length=30)
    lastname = models.CharField("Last name", max_length=30)
    department = models.CharField("Department or School", max_length=50)
    email = models.EmailField("Email")
    web = models.URLField("Web link", blank=True)
    interests = models.TextField("Research interests", blank=True)

    def __str__(self):
        return self.firstname +  " " + self.lastname


class Project(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    short = models.TextField("Short description", blank=True)
    honours = models.BooleanField("Suitable for Honours", default=True)
    mds = models.BooleanField("Suitable for MDS", default=True)
    engineering = models.BooleanField("Suitable for Engineering")
    numstudents = models.CharField("Number of Students", max_length=30, blank=True)
    #primary = models.CharField("Primary Supervisor", max_length=50)
    primary = models.ForeignKey(Supervisor, on_delete=models.CASCADE, blank=True, null = True)
    cosupervisors = models.TextField("Co-supervisors", blank=True)
    external = models.TextField("External supervisors/mentors/sponsors", blank=True)
    link = models.URLField("Research Link", blank = True)
    references = models.TextField("Sample references", blank=True)
    created = models.DateField("Date Created", auto_now_add = True)
    modified = models.DateField("Last Modified", auto_now = True)
    current_date = models.DateField("Current Date", default = date.today)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

