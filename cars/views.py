from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    all_cars = Car.objects.order_by('-created_on')
    paginator = Paginator(all_cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


    data = {
        'all_cars':paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/cars.html', data)

def car_details(request, id):
    single_cars = get_object_or_404(Car, pk=id)
    data = {
        'single_cars': single_cars,
    }
    return render(request, 'cars/car_details.html', data)

def search(request):
    cars =  Car.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            cars = Car.objects.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']

        if model:
            cars = Car.objects.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            cars = Car.objects.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']

        if year:
            cars = Car.objects.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']

        if body_style:
            cars = Car.objects.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = cars.filter(price__gte = min_price, price__lte = max_price)


    data = {
        'cars': cars,
    }

    return render(request, 'cars/search.html', data)