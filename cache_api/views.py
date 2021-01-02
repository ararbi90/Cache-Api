from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Log
from .cache.cache_set import CacheSet

# Create cache
cache = CacheSet(500)
users = ["ahmed", "danny", "jon", "sam", "harry", "ron"];
for user in users:
    for i in range(10):
        cache.add(user, str(i), str(i))

# Create your views here.
def index(request):
    return render(request, "html/index.html")

def get(request):
    if request.method == "GET":
        print(request.GET)
        if "user" not in request.GET or "key" not in request.GET:
            return JsonResponse({"error":"incorrect request"})
        user = request.GET["user"]
        key = request.GET["key"]
        l = Log(user_name=user,pub_date=timezone.now())
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
        l = Log(user_name=user,pub_date=timezone.now())
        l.save()
        print(value)
        cache.add(user, key, value)
        return JsonResponse({"user":user, "key":key, "value":value}) 
    else:
        return JsonResponse({"error":"incorrect request"}) 
    

