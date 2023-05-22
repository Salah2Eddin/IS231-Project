# Generated by Django 4.2.1 on 2023-05-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_student_birthdate_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('GN', 'General'), ('AI', 'Artificial Intelligence'), ('CS', 'Computer Science'), ('IS', 'Information Systems'), ('DS', 'Decision Support'), ('IT', 'Information Technology')], max_length=3, null=True),
        ),
    ]
