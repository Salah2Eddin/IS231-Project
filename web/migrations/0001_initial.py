# Generated by Django 4.2.1 on 2023-05-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=13)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('status', models.CharField(choices=[('Y', 'Active'), ('N', 'Not active')], max_length=1)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('level', models.IntegerField()),
                ('department', models.CharField(max_length=3, null=True)),
                ('birthDate', models.DateField(null=True)),
            ],
        ),
    ]
