from django.contrib.auth.decorators import login_required
from rest_framework import generics
from product.serializer import ProductSerializerHome
from product.models import Product
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePageApi(generics.ListAPIView):
    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializerHome

    
    