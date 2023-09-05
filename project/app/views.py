from django.shortcuts import render, redirect
from .models import Employee
from .forms import UserRegistrationForm

# Create your views here.
def base(request):
    employee_list = Employee.objects.all()
    employee_details = {"employee_list": employee_list}
    
    return render(request, "base.html", employee_details)

def addStaff(request):    
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        number = request.POST.get('number')
        title = request.POST.get('title')
        
        dbQuery = Employee(
            name = name,
            gender = gender,
            email = email,
            number = number,
            title = title
        )
        
        dbQuery.save()
        return redirect("/")
        
    return render(request, "base.html")

def deleteStaff(request, id):
    employee_list = Employee.objects.get(id=id)
    employee_list.delete()
    
    return redirect("/")

def editStaff(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        number = request.POST.get('number')
        title = request.POST.get('title')
        
        edit_employee_list = Employee.objects.get(id=id)
        edit_employee_list.name = name
        edit_employee_list.gender = gender
        edit_employee_list.email = email
        edit_employee_list.number = number
        edit_employee_list.title = title
        edit_employee_list.save()
        return redirect("/")

    employee_list = Employee.objects.get(id=id)
    employee_details = {"employee_list": employee_list}
    
    return render(request, "edit.html", employee_details)

def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}

    return render(request, "registration/register.html", context)