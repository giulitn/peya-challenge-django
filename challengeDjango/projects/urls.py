from django.urls import path, include
from projects.views import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProjectViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]