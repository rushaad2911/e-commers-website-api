from django.urls import path
from .views import ProductCreateApiView

urlpatterns = [
    
    path('create/',ProductCreateApiView.as_view(),name='productcreateapi'),
]