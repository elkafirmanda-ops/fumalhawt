from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'alquran', views.AlquranViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]