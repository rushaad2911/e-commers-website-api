from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SellerAccount, UserAccount,SellerAccount

class CustomUserAdmin(UserAdmin):
    
    

    model = UserAccount
    list_display = ['username', 'password', 'first_name', 'last_name', 'is_active','is_superuser']
        
        

class UserAdmin(UserAdmin):
    
    model = SellerAccount
    list_display = ['username','password','is_seller','shop_name']
    
admin.site.register(UserAccount, CustomUserAdmin)

admin.site.register(SellerAccount,UserAdmin)