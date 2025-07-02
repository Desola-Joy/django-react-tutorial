from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewset, basename='project')
# urlpatterns = router.urls


urlpatterns = [
    path('home/', home, name='home'),                 
    path('', include(router.urls)), 
]