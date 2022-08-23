from django.urls import path,include

from .views import HomePageApi


urlpatterns = [
    
    path('',HomePageApi.as_view(),name='homepageapi'),
    path('product/',include('product.urls')),
    
    
]