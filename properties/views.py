# properties/views.py

from django.http import JsonResponse
from .utils import get_all_properties
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    queryset = get_all_properties()
    data = list(queryset.values("id", "title", "description", "price", "location", "created_at"))
    return JsonResponse({"count": len(data), "results": data})