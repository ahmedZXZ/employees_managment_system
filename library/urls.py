from django.urls import path
from . import views



urlpatterns = [
    path('', views.index , name='index'),
    path('add_new_employee', views.add_new_employee, name='add_new_employee'),
    path('view_employees', views.view_employees, name='view_employees'),
    path('add_new_department', views.add_new_department, name='add_new_department'),
    path('view_departments', views.view_departments, name='view_departments'),
    path('delete/employee/<int:EmployeeID>', views.delete_employee, name='delete_employee'),
    path('edit/employee/<int:EmployeeID>', views.edit_employee, name='edit_employee'),
    path('delete/department/<int:DepartmentID>', views.delete_department, name='delete_department'),
    path('edit/department/<int:DepartmentID>', views.edit_department, name='edit_department'),
    
]
