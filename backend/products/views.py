from django.shortcuts import render
from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):

        '''

        You want to modify the validated data before saving.

        You want to add additional fields (like the logged-in user).

        You want to conditionally update fields (like your example with content).

        You want to trigger side effects, like sending a signal, logging, sending an email, etc.
        '''

        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        # send signal
    
    # class ProductListAPIView(generics.ListAPIView):
    #     queryset = Product.objects.all()
    #     serializer_class = ProductSerializer


@api_view(["GET","POST"])
def product_alt_view(request,pk = None , *args,**kwargs):
        method = request.method 
        

        if method == 'GET':
            
            if pk is not None:
                 #detailview
                 obj = get_object_or_404(Product,pk = pk)
                 data = ProductSerializer(obj).data
                 return Response(data)
            else:
                #listview
                queryset = Product.objects.all()
                data = ProductSerializer(queryset,many = True).data
                return Response(data)



        if method == 'POST':

            serializer = ProductSerializer(data = request.data) #request.data = post request ma k data mokalye e
            if serializer.is_valid(raise_exception=True):
                title = serializer.validated_data.get('title')
                content = serializer.validated_data.get('content') or None
                if content is None:
                    content = title
                serializer.save(content = content)
                return Response(serializer.data)
            return Response({"invalid":"not good data"},status=400 )
        

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):

        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
        


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
