from django.urls import path
from .views import ProductCreateApiView,ProductDeleteApiView,ProductEditApiView



urlpatterns = [
    
    path('create/',ProductCreateApiView.as_view(),name='productcreateapi'),
    path('delete/<uuid:pk>/',ProductDeleteApiView.as_view(),name='productdeleteapi'),
    path('edit/<uuid:pk>/',ProductEditApiView.as_view(),name='producteditapi'),
]