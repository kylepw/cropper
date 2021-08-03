"""cropperapi URL Configuration"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import URLViewSet


router = DefaultRouter()
router.register(r'', URLViewSet)

urlpatterns = [
    path('', include(router.urls)),
]