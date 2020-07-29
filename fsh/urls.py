from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.schemas import get_schema_view

from fsh import __version__
from fsh.apps.snippet.views import UserViewSet
from fsh.apps.snippet.urls import router as snippet_router

router = routers.DefaultRouter()
router.registry.extend(snippet_router.registry)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('schema/', get_schema_view(
        title='Full Stack Hero',
        description="API for all things …",
        version=__version__
    ), name='openapi-schema'),
]
