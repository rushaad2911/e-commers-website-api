from django.urls import path,include
from .views import CreateUser,CreateSeller

urlpatterns = [
    
    path('create/',CreateUser.as_view(),name='user'),
    path('',include('allauth.urls')),
    path('seller/',CreateSeller.as_view(),name='seller')
    
]