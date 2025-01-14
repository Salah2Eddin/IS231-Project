# Generated by Django 4.2.1 on 2023-05-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('General', 'GN'), ('Artificial Intelligence', 'AI'), ('Computer Science', 'CS'), ('Information Systems', 'IS'), ('Decision Support', 'DS'), ('Information Technology', 'IT')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Active', 'Y'), ('Not active', 'N')], default='Y', max_length=20),
        ),
    ]
