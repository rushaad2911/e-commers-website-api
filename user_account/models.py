from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django import forms
from django.contrib.auth.hashers import make_password



class UserAccount(AbstractUser):
    
    id = models.UUIDField(
        
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    
    )
    



class SellerAccount(UserAccount):
    
    is_seller = models.BooleanField(default=True,null=True,blank=True)
    shop_name = models.CharField(max_length=30,null=True,blank=True)
    
    def save(self,**kwargs):
        
        self.password = make_password(self.password)
        super().save(**kwargs)
        
        
        
class BuyerAccount(UserAccount):
    
    is_buyer = models.BooleanField(default=True)
    
    
    
    def save(self,**kwargs):
        
        self.password = make_password(self.password)
        super().save(**kwargs)