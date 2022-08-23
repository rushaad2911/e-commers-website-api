from rest_framework import generics
from product.serializer import ProductSerializer
from product.models import Product

class HomePageApi(generics.ListAPIView):
    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer