# Generated by Django 4.2.1 on 2023-05-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_student_department_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('AI', 'Artificial Intelligence'), ('CS', 'Computer Science'), ('IS', 'Information Systems'), ('DS', 'Decision Support'), ('IT', 'Information Technology')], max_length=8, null=True),
        ),
    ]
