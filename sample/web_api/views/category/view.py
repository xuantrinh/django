from rest_framework import generics, status, permissions
from ...models import Category
from ...serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from datetime import datetime

class CategoryList(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=all)
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    def post(self, request):
        data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'created_at' : datetime.now(),
            'updated_at': datetime.now()
        }
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryDetail(GenericAPIView):
    
    def get(self, request, pk):
        queryset = Category.objects.get(id=pk)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        category = Category.objects.get(id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
