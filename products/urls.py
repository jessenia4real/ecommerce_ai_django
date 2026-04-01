from django.urls import path
from .views import ProductListView, ProductDetailView, CategoryListView, ProductsByCategoryView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/category/<str:category_slug>/', ProductsByCategoryView.as_view(), name='products-by-category'),
]
