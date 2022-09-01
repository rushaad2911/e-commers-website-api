from django.urls import path,include
from .views import CreateUser

urlpatterns = [
    
    path('create/',CreateUser.as_view(),name='user'),
    path('',include('allauth.urls')),
    
]