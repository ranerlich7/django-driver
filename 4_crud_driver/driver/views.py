from django.http import HttpResponse
from django.shortcuts import render, redirect

from driver.models import Driver, Team

# Create your views here.

# def index():
# Driver.objects.all()


def drivers(request):
    # get all drivers from DB
    search_text = request.GET.get('search_text')
    all_drivers = Driver.objects.all()
    # filter all drivers by search_text field - that comes from the form
    if search_text:
        all_drivers = all_drivers.filter(username__icontains=search_text)
    return render(request, 'drivers.html', {'all_drivers': all_drivers})


def add_driver(request):
    print("--- add driver enter")
    # GET request - return the form
    if request.method == "GET":
        print("--* GET")
        # extra - get all teams and select which teams this driver belongs to
        teams = Team.objects.all()
        return render(request, 'add_driver.html', {'teams': teams})
    # POST request - add the driver
    elif request.method == 'POST':
        print("--* POST")
        username = request.POST.get('username')
        password = request.POST.get('password')
        # getting team_id from form. then getting the team object from DB (this is neccesary to save the driver with this team)
        team_id = request.POST.get('selected_team')
        team = Team.objects.get(pk=team_id)
        age = request.POST.get('age')
        print(f"--* user:{username} age:{age} ")
        driver = Driver(username=username, password=password,
                        age=age, team=team)
        driver.save()
        return redirect('all_drivers')
