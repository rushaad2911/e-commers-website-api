from urllib import request
from rest_framework import serializers
from .models import  UserAccount
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction


        
class UserAccountCreateSerializer(RegisterSerializer):
    
    
    seller_account = serializers.BooleanField(default=False)
        
    # model = UserAccount
    # fields = ['username','password','seller_account']
    
    
    @transaction.atomic      
    def save(self,request):
        
        user = super().save(request)
        # user.username=self.data.get('username')
        user.seller_account=self.data.get('seller_account')
        # user.password=self.data.get('password')
        user.save()
        return user
           
           