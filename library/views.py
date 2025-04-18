from django.shortcuts import render , redirect , HttpResponse
from .forms import EmployeeForm , DepartmentForm
from .models import Employee , Department
from django.contrib import messages

# Create your views here.
def index(request):
    print("Index view called")
    #return HttpResponse("Welcome to the Django project! This is a plain text response.")
    return render(request,'index.html')

def add_new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/view_employees')
    else:
        form = EmployeeForm()
        return (render(request,'add_new_employee.html' , {'form':form}))

def view_employees(request):
    employees = Employee.objects.order_by('EmployeeID')
    return (render(request,'view_employees.html' , {'employees':employees} ))

def add_new_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/view_departments')
    else:
        form = DepartmentForm()
        return (render(request,'add_new_department.html', {'form':form}))

def view_departments(request):
    departments = Department.objects.order_by('DepartmentID')
    return (render(request,'view_departments.html', {'departments':departments} ))

# ... existing code ...

def delete_employee(request, EmployeeID):
    """
    Delete an employee with the given EmployeeID
    """
    try:
        # Get the employee object
        employee = Employee.objects.get(EmployeeID=EmployeeID)
        # Store the name for confirmation message
        employee_name = employee.Name
        # Delete the employee
        employee.delete()
        # Redirect with success message
        messages.success(request, f'Employee "{employee_name}" has been deleted successfully.')
    except Employee.DoesNotExist:
        # Handle case where employee doesn't exist
        messages.error(request, f'Employee with ID {EmployeeID} not found.')
    
    # Redirect back to the employees list
    return redirect('view_employees')

def edit_employee(request, EmployeeID):
    try:
        if request.method == "POST":
            emp =Employee.objects.get(EmployeeID=request.session['EmployeeID'])    
            form = EmployeeForm((request.POST),instance=emp)
            if form.is_valid():
                form.save()
            del request.session['EmployeeID']
            return redirect("/view_employees")
        else:
            employee_to_edit=Employee.objects.get(EmployeeID=EmployeeID)
            employee=EmployeeForm(instance=employee_to_edit)
            request.session["EmployeeID"]=employee_to_edit.EmployeeID
            return render(request,'edit_employee.html',{'employee':employee})
    except Exception as error:
        print(f"{error} occured at edit_employee_data view")



def delete_department(request, DepartmentID):
    """
    Delete a department with the given DepartmentID
    """
    try:
        # Get the department object
        department = Department.objects.get(DepartmentID=DepartmentID)
        # Store the name for confirmation message
        department_name = department.Dept_Name
        # Delete the department
        department.delete()
        # Redirect with success message
        messages.success(request, f'Department "{department_name}" has been deleted successfully.')
    except Department.DoesNotExist:
        # Handle case where department doesn't exist
        messages.error(request, f'Department with ID {DepartmentID} not found.')
    
    # Redirect back to the departments list
    return redirect('view_departments')

def edit_department(request, DepartmentID):
    try:
        if request.method == "POST":
            dept = Department.objects.get(DepartmentID=request.session['DepartmentID'])    
            form = DepartmentForm((request.POST), instance=dept)
            if form.is_valid():
                form.save()
            del request.session['DepartmentID']
            return redirect("/view_departments")
        else:
            department_to_edit = Department.objects.get(DepartmentID=DepartmentID)
            department = DepartmentForm(instance=department_to_edit)
            request.session["DepartmentID"] = department_to_edit.DepartmentID
            return render(request, 'edit_department.html', {'department': department})
    except Exception as error:
        print(f"{error} occurred at edit_department_data view")
        return redirect('view_departments')