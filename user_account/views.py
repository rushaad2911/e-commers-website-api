from django.shortcuts import render
from rest_framework import generics
from .models import UserAccount,SellerAccount,BuyerAccount
from .serializers import UserCreateSerializers,SellerCreateSerializer,BuyerCreateSerializer
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password



class CreateUser(generics.CreateAPIView):
    
    queryset = UserAccount
    serializer_class = UserCreateSerializers
    
    
class CreateSeller(generics.CreateAPIView):
    
    queryset = SellerAccount
    serializer_class = SellerCreateSerializer
    
  
    
    
    def post(self,*args,**kwargs):

    
        super().post(*args,**kwargs)
        return HttpResponseRedirect(reverse_lazy('account_login'))
    
    
    
    
class CreateBuyer(generics.CreateAPIView):
    
    queryset = BuyerAccount
    serializer_class = BuyerCreateSerializer
    
    
    def post(self,*args,**kwargs):
    
    
        super().post(*args,**kwargs)
        return HttpResponseRedirect(reverse_lazy('account_login'))
    