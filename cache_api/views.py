from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Log
from .cache.cache_set import CacheSet

# Create cache
cache = CacheSet(500)

# Create your views here.
def index(request):
    return render(request, "html/index.html")

def get(request):
    if request.method == "GET":
        if "user" not in request.GET or "key" not in request.GET:
            return JsonResponse({"error":"incorrect request"})
        user = request.GET["user"]
        key = request.GET["key"]
        l = Log(user_name=user,pub_date=timezone.now(), user_method=request.method)
        l.save()
        value = cache.get(user, key)
        return JsonResponse({"user":user, "key":key, "value":value}) 
    else:
        return JsonResponse({"error":"incorrect request"}) 

@csrf_exempt
def add(request):
    if request.method == "POST":
        if "user" not in request.POST or "key" not in request.POST:
            return JsonResponse({"error":"incorrect request"})
        user = request.POST["user"]
        key = request.POST["key"]
        value = request.POST["value"]
        l = Log(user_name=user,pub_date=timezone.now(), user_method=request.method)
        l.save()
        cache.add(user, key, value)
        return JsonResponse({"user":user, "key":key, "value":value}) 
    else:
        return JsonResponse({"error":"incorrect request"}) 
    

