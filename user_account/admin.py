from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  UserAccount

class CustomUserAdmin(UserAdmin):
    
    

    model = UserAccount
    list_display = ['username', 'id','password', 'seller_account', 'is_active','is_superuser']
        
        

# class SellerAdmin(UserAdmin):
    
#     model = SellerAccount
#     list_display = ['username','password','is_seller','shop_name']
    
    
# class BuyerAdmin(UserAdmin):
#     model = BuyerAccount
#     list_display = ['username','password','is_seller']
    
admin.site.register(UserAccount, CustomUserAdmin)

# admin.site.register(SellerAccount,SellerAdmin)

# admin.site.register(BuyerAccount,BuyerAdmin)