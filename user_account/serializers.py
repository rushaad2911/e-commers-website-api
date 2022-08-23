from rest_framework import serializers
from .models import UserAccount

class UserCreateSerializers(serializers.ModelSerializer):
    
    class Meta():
        
        model = UserAccount
        fields = ['username','password','email']