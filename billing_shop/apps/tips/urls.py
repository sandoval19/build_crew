
from django.urls import include, path
from rest_framework import routers

from apps.tips.views.tips_views import TipsView

router = routers.DefaultRouter()
router.register(r'tips', TipsView)

urlpatterns = [path('', include(router.urls)), ]
