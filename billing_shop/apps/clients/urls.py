
from django.urls import include, path
from rest_framework import routers

from apps.clients.views.client_view import ClientViews


router = routers.DefaultRouter()
router.register(r'clients', ClientViews)

urlpatterns = [path('', include(router.urls)), ]
