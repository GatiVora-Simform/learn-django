import json
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def api_home(request,*args,**kwargs):

    print(request.GET) #to get query params

    body = request.body #byte string of json data

    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    
    return JsonResponse(data)  # return a json response