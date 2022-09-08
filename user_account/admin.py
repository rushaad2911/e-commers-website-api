from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SellerAccount, UserAccount,SellerAccount,BuyerAccount

class CustomUserAdmin(UserAdmin):
    
    

    model = UserAccount
    list_display = ['username', 'password', 'first_name', 'last_name', 'is_active','is_superuser']
        
        

class SellerAdmin(UserAdmin):
    
    model = SellerAccount
    list_display = ['username','password','is_seller','shop_name']
    
    
class BuyerAdmin(UserAdmin):
    model = BuyerAccount
    list_display = ['username','password','is_buyer']
    
admin.site.register(UserAccount, CustomUserAdmin)

admin.site.register(SellerAccount,SellerAdmin)

admin.site.register(BuyerAccount,BuyerAdmin)