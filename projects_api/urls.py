from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects_api import views

router = DefaultRouter()
router.register('personel', views.PersonelListViewSet)
router.register('project', views.ProjectListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
