from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('list', ListViewSet)
router.register('item', ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
