from tkinter import S
from django.shortcuts import render
from .models import Product
from .serializer import CreateProductSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# from seller_account.models import SellerAccount



class ProductCreateApiView(generics.CreateAPIView):
    
    
    # def get(self,*args,**kwargs):
        
    #     if isinstance(self.request.user,SellerAccount):
           
    #         return HttpResponseRedirect(reverse_lazy('homepageapi'))
            
    #     else:
    #         return HttpResponseRedirect(reverse_lazy('createselleraccount'))
            

        
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    # permission_classes = []       create a custom permission class
    
    
    def perform_create(self, serializer):                
        # used to add extra data when creating a new object in the database --will not execute if u override create
        serializer.save(seller_id=self.request.user)
        
    
    def post (self,*args,**kwargs):
        super().post(*args,**kwargs)
        return HttpResponseRedirect(reverse_lazy('homepageapi'))
    
    
    
        
        
class ProductDeleteApiView(generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    # lookup_field = 'product_id'
    # permission_classes = []
    
    
    def perform_create(self, serializer):                
        # used to add extra data when creating a new object in the database --will not execute if u override create
        serializer.save(seller_id=self.request.user)