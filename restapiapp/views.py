from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

# tCreate your views here
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/product-list/',
        #it contains product details of a particular product so we used id here
        'Detail View':'/product-detail/<int:id>/',
        'Create':'/product-create/',
        #to upadate particular product through id
        'Update':'/product-update/<int:id>/',
        #to delete particular product
        'Delete':'/product-create/<int:id>/',
    }
    return Response(api_urls)
#to get all the information that we added from admin panel
@api_view(['GET'])
def ShowAll(request):
    products=Product.objects.all()
    #many=true because we will have many product
    serializer=ProductSerializer(products, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def ViewProduct(request, pk):
    #to see a single product based on id
    product=Product.objects.get(id=pk)
    serializer=ProductSerializer(product, many=False)
    return Response(serializer.data)
    #to post the data we created we use post here
@api_view(['POST'])
def CreateProduct(request):
    #product that we need to create is the data that we pass
    serializer=ProductSerializer(data=request.data)
    #to check whether the data we passed is in valid format
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def UpdateProduct(request,pk):
    #to update particular product through id
    product=Product.objects.get(id=pk)
    #data that we pass
    serializer=ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def DeleteProduct(request,pk):
    #to delete particular product we used id
    product=Product.objects.get(id=pk)
    product.delete()
    return Response('Items deleted successfully')
