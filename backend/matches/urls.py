from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, NewsViewSet

router = DefaultRouter()
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
