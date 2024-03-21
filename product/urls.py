from django.urls import path, include

from product.views import ProductDetailView, ProductDetailAPI

app_name = 'product'

urlpatterns = [
    path('detail/', ProductDetailView.as_view(), name='detail'),
    path('<int:product_id>/', ProductDetailAPI.as_view()),
]














