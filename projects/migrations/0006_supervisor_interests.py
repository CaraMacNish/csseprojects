# Generated by Django 4.1 on 2022-12-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_project_short"),
    ]

    operations = [
        migrations.AddField(
            model_name="supervisor",
            name="interests",
            field=models.TextField(blank=True, verbose_name="Research interests"),
        ),
    ]