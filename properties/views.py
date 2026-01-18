from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

# Cache for 15 minutes (60 sec * 15)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values("id", "name", "price", "location")  # adjust fields
    return JsonResponse(list(properties), safe=False)


def property_list(request):
    properties = get_all_properties()
    # Convert to dict for JSON response
    properties_data = [
        {"id": prop.id, "name": prop.name, "price": prop.price, "location": prop.location}
        for prop in properties
    ]
    return JsonResponse(properties_data, safe=False)
