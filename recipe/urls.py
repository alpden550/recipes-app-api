from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('tags', views.TagViewSet, 'tag')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]