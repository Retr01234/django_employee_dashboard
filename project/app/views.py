from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def addStaff(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        number = request.POST.get('number')
        title = request.POST.get('title')
        
    return render(request, "index.html")