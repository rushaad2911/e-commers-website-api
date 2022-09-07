from rest_framework import serializers
from .models import UserAccount,SellerAccount
from django import forms


class UserCreateSerializers(serializers.ModelSerializer):
    
    class Meta():
        
        model = UserAccount
        fields = ['username','password','email']
        
        

class SellerCreateSerializer(serializers.ModelSerializer):
    
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        
        model = SellerAccount
        fields  =['username','password','email','shop_name']