from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserAccount
    list_display = ['username', 'password', 'first_name', 'last_name', 'is_active','is_superuser']
        
        
        
admin.site.register(UserAccount, CustomUserAdmin)