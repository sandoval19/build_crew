
from django.urls import include, path
from rest_framework import routers

from apps.products.views.products_views import ProductsView

router = routers.DefaultRouter()
router.register(r'products', ProductsView)

urlpatterns = [path('', include(router.urls)), ]
