from django.urls import path,include
from .views import CreateUser,CreateSeller,CreateBuyer

urlpatterns = [
    
    path('create/',CreateUser.as_view(),name='createuser'),
    path('',include('allauth.urls')),
    path('seller/',CreateSeller.as_view(),name='createseller'),
    path('buyer/',CreateBuyer.as_view(),name='createbuyer'),
    
]