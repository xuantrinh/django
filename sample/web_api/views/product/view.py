import imp
from requests import request
from rest_framework import generics, status, permissions
from ...models import Product, Category
from ...serializers import ProductSerializer, ProductCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from datetime import datetime
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView

class ProductView():

    product_create_response = openapi.Response('response description', ProductSerializer)
    @swagger_auto_schema(method='GET', responses= {200: product_create_response})
    @api_view(['GET'])
    @permission_classes([permissions.IsAuthenticated])
    def get_products(self):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=all)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method='POST', request_body=ProductCreateSerializer, responses= {200: product_create_response})
    @api_view(['POST'])
    @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
    def create_product(request):
        data = {
                'category': request.data.get('category_id'), 
                'name': request.data.get('name'), 
                'title': request.data.get('title'), 
                'price': request.data.get('price'),
                'image': request.data.get('image'),
                'score': request.data.get('score'),
                'created_at' : datetime.now(),
                'updated_at': datetime.now()
            }
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetail():
    product_response = openapi.Response('response description', ProductSerializer)
    @swagger_auto_schema(method='DELETE', responses= {200: 'Delete successfully'})
    @api_view(['DELETE'])
    @permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
    def delete_product(request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(method='GET', responses= {200: product_response})
    @api_view(['GET'])
    @permission_classes([permissions.IsAuthenticated])
    def get_product(request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


    