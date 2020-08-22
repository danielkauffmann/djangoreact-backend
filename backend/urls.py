from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views

from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('list', ListViewSet, basename='list')
router.register('item', ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
