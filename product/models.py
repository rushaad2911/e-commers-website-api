from django.db import models
import uuid 
from user_account.models import UserAccount


class Gerens(models.Model):
    
    geren = models.CharField(max_length=50)
    def __str__(self):
        return self.geren
  
  
  
    
class Product(models.Model):
   
    
    seller_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE,blank=True, null=True)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_geren = models.ManyToManyField(Gerens,blank=True)
    product_title = models.CharField(max_length=300)
    product_price = models.IntegerField() 
    product_images = models.ImageField(upload_to='product_images/')
    product_description = models.TextField()
    product_features_spesification = models.TextField(null = True,blank = True)
    
    
    
    def __str__(self):
        return self.product_title
    
    
    def delete(self,*args,**kwargs):
        self.product_images.delete()
        return super().delete(*args,**kwargs)
    
 
 

class address(models.Model):
    
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.IntegerField()
    user_adress = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    street_1 = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100)