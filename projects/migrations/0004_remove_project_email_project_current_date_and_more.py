# Generated by Django 4.1 on 2022-12-16 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_primary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="email",
        ),
        migrations.AddField(
            model_name="project",
            name="current_date",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Current Date"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="references",
            field=models.TextField(blank=True, verbose_name="Sample references"),
        ),
    ]
