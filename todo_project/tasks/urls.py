from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefuaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', incluide(router.urls)),
]