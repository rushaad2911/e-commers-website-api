from email import message
from rest_framework import permissions


class ProductCreatPermission(permissions.BasePermission):
    
    message = 'you need a seller account for this'
    
    def has_permission(self, request, view):
        
        if self.request.user.seller_account :
            print('hi')
        else:
            print('bye')
        
        return request.user
            
        