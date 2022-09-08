from rest_framework import serializers
from .models import BuyerAccount, UserAccount,SellerAccount
from django import forms


class UserCreateSerializers(serializers.ModelSerializer):
    
    class Meta():
        
        model = UserAccount
        fields = ['username','password','email']
        
        

class SellerCreateSerializer(serializers.ModelSerializer):
    
  
    class Meta():
        
        model = SellerAccount
        fields = ['username','password','email','shop_name']
        
        
class BuyerCreateSerializer(serializers.ModelSerializer):
    class Meta():
        
        model = BuyerAccount
        fields = ['username','password','email']