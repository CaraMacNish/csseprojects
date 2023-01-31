# Generated by Django 4.1.5 on 2023-01-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_numstudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='other',
            field=models.CharField(blank=True, max_length=20, verbose_name='Other (please specify)'),
        ),
        migrations.AddField(
            model_name='project',
            name='se',
            field=models.BooleanField(default=True, verbose_name='Suitable for Software Engineering'),
        ),
        migrations.AlterField(
            model_name='project',
            name='engineering',
            field=models.BooleanField(default=False, verbose_name='Suitable for Engineering'),
        ),
        migrations.AlterField(
            model_name='project',
            name='numstudents',
            field=models.CharField(blank=True, max_length=20, verbose_name='Number of Students'),
        ),
    ]
