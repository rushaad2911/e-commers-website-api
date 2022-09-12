from calendar import c
from django.urls import path,include
from .views import CreateSeller,CreateUserAccoun

urlpatterns = [
    
   
    path('',include('dj_rest_auth.urls')),
    path('signup/',include('dj_rest_auth.registration.urls')),
    path('<uuid:pk>/',CreateSeller.as_view(),name='createseller'),
    
]