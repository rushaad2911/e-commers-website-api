from django.shortcuts import render
from .models import Product
from .serializer import CreateProductSerializer,EditProductSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin

from django.contrib.auth.models import Permission
from .permissions import ProductCreatPermission


class ProductCreateApiView(LoginRequiredMixin,
                        #    PermissionRequiredMixin,
                           generics.CreateAPIView):
    
    

        
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    login_url = 'rest_login'
    # permission_required = [ProductCreatPermission]
    
    
    def perform_create(self, serializer):                
        # used to add extra data when creating a new object in the database --will not execute if u override create
        serializer.save(seller_id=self.request.user)
        
    
    def post (self,*args,**kwargs):
        
        self.seller_id=self.request.user
        super().post(*args,**kwargs)
        return HttpResponseRedirect(reverse_lazy('homepageapi'))
    
    
        
    
    
        
        
class ProductDeleteApiView(LoginRequiredMixin,UserPassesTestMixin,generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    login_url = 'rest_login'
    # permission_classes = []
    
    
    def perform_create(self, serializer):                
        # used to add extra data when creating a new object in the database --will not execute if u override create
        serializer.save(seller_id=self.request.user)
        
        
    def test_func(self):
        
        obj = self.get_object()
        return obj.seller_id == self.request.user
    
    
        
class ProductEditApiView(LoginRequiredMixin,UserPassesTestMixin,generics.RetrieveUpdateAPIView):
    
    queryset = Product
    serializer_class = EditProductSerializer
    login_url = 'rest_login'
    
    def test_func(self):
        
        obj = self.get_object()
        return obj.seller_id == self.request.user