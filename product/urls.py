from django.urls import path
from .views import ProductCreateApiView,ProductDeleteApiView,ProductDetailApiView



urlpatterns = [
    
    path('create/',ProductCreateApiView.as_view(),name='productcreateapi'),
    path('delete/<uuid:pk>/',ProductDeleteApiView.as_view(),name='productdeleteapi'),
    path('<uuid:pk>/',ProductDetailApiView.as_view(),name='productdetailapi'),
]