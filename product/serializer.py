from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Product
        fields = ('product_id', 'product_title', 'product_price', 'product_geren','seller_id')
        

class ProductSerializerHome(serializers.ModelSerializer):
    class Meta:
        
        model = Product
        fields = ('product_id', 'product_title', 'product_price', 'product_geren','seller_id','seller_id')
       
        
        
    
class CreateProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('product_title', 'product_price', )
        
        
        


class EditProductSerializer(serializers.ModelSerializer):
    class Meta():
        
        model = Product
        fields = ('product_title','product_price','product_geren','product_description','product_features_spesification')