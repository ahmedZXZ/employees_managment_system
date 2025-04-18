from django.db import models

# Create your models here.

class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    Dept_Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Dept_Name

    class Meta:
        verbose_name_plural = "Departments"

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Dept_Name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Employees"