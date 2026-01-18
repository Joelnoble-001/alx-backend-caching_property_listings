from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

# Cache for 15 minutes (60 sec * 15)

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    # Convert queryset to a list of dictionaries
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": float(prop.price),
            "location": prop.location,
            "created_at": prop.created_at.isoformat(),
        }
        for prop in properties
    ]
    # Return JSON response
    return JsonResponse({"properties": data})


def property_list(request):
    properties = get_all_properties()
    # Convert to dict for JSON response
    properties_data = [
        {"id": prop.id, "name": prop.name, "price": prop.price, "location": prop.location}
        for prop in properties
    ]
    return JsonResponse(properties_data, safe=False)


