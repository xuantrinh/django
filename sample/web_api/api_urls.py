from django.urls import path
from .views import (
    CategoryList,
    CategoryDetail,
    ProductDetail,
    ProductView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('products', ProductView.get_products, name='GET'),
    path('products/create',  ProductView.create_product, name= 'POST'),
    path('products/<int:id>', ProductDetail.get_product),
    path('products/delete/<int:id>', ProductDetail.delete_product)
]


