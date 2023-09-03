from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    employee_list = Employee.objects.all()
    employee_details = {"employee_list": employee_list}
    
    return render(request, "index.html", employee_details)

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
        
    return render(request, "index.html")