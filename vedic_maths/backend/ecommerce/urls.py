from django.urls import path, include
from rest_framework import routers

from .views import ( productsView, ProductCategoryViewSet)


router = routers.DefaultRouter()

router.register('products', productsView, 'products')
router.register('ProductCategory', ProductCategoryViewSet, 'ProductCategory')




urlpatterns = [
   path('', include(router.urls)),

]
