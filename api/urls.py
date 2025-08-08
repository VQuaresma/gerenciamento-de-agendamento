from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgendaViewSet


router = DefaultRouter()
router.register(r'agendas', AgendaViewSet, basename='agenda')
router.register(r'usuarios', AgendaViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]