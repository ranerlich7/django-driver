from django.http import HttpResponse
from django.shortcuts import render

from driver.models import Driver

# Create your views here.

# def index():
# Driver.objects.all()


def drivers(request):
    # get all drivers from DB
    all_drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'all_drivers': all_drivers})
