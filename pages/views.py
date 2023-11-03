from django.shortcuts import render, get_object_or_404
from . models import Team
from cars.models import Car

def home(request):
    teams =  Team.objects.all()
    featured_cars = Car.objects.order_by('created_on').filter(is_featured=True)
    latest_cars = Car.objects.order_by('created_on')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars':latest_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams =  Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
# Create your views here.
