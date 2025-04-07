import json
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from rest_framework import generics

# @api_view(["GET","POST"])
# def api_home(request,*args,**kwargs):
#     # print(request.GET) #to get query params
#     # body = request.body #byte string of json data
#     # data = {}
#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass
#     # print(data)
    
#     # return JsonResponse(data)  # return a json response

#     ############################################################
#     # model_data = Product.objects.all().order_by("?").first()
#     # data = {}
#     # if model_data:
#     #     data['title'] = model_data.title
#     #     data['content'] = model_data.content
#     #     data['price'] = model_data.price
#     # return JsonResponse(data)\

#     ###########################################################

#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)

################################################################################################################
@api_view(["POST"])
def api_home(request,*args,**kwargs):

    serializer = ProductSerializer(data = request.data) #request.data = post request ma k data mokalye e
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400 )

################################################################################################################

