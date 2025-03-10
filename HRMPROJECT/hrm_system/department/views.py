from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from .forms import DepartmentForm


# View all departments
def department_list(request):
    departments = Department.objects.filter(status='active')
    query = request.GET.get('q')
    if query:
        departments = departments.filter(dept_name__icontains=query)
    return render(request, 'department_list.html', {'departments': departments})

# Add a new department
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

# Update a department
def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form})

# Soft delete a department
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.status = 'inactive'
        department.save()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': department})


def home(request):
    return render(request, 'home.html')