from django.test import TestCase
from .models import Product
from user_account.models import SellerAccount
from django.contrib.auth.models import Permission

class CreateProductTest(TestCase):
    
    def setUp(self):
        
        self.user = SellerAccount.objects.create_user(
            
            username = 'test_seller',
            password = 'testsellerpassword',
            email = 'test_seller@gmail.com'
            
        )
        
        self.permission = Permission.objects.get(codename='is_seller')
        
        self.product = Product.objects.create(
            
            seller_id = self.user,
            product_title = 'test_product',
            product_price = 100,
            product_description = 'test discription'
            
        )
        
        
    def test_product_creation(self):
        
        self.client.login(
            email='test_seller@gmail.com',
            username='test_seller',
            password = 'testsellerpassword'
        )
        
        
        self.user.user_permissions.add(self.permission)
        
        res = self.client.get('/product/create')
        
        self.assertEqual(self.user.username,'test_seller')
        self.assertEqual(res.status_code,200)

