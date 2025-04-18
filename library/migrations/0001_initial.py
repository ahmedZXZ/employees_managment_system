# Generated by Django 5.2 on 2025-04-18 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentID', models.AutoField(primary_key=True, serialize=False)),
                ('Dept_Name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Dept_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.department')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
