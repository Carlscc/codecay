from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, county_choices

from listings.models import Listing
from listings.models import Host

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'county_choices': county_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    hosts = Host.objects.all()

    context = {
        'hosts': hosts
    }

    return render(request, 'pages/about.html', context)

