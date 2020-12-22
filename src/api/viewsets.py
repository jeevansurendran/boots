from api.serializers import CategorySerializer, ProductSerializer
from api.models import Category, Product
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
