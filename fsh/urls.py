from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.schemas import get_schema_view

from fsh import __version__
from fsh.apps.snippet.views import UserViewSet
from fsh.apps.snippet.urls import router as snippet_router

router = routers.DefaultRouter()
router.registry.extend(snippet_router.registry)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/auth/', include('rest_auth.urls')),
    path('user/auth/signup/', include('rest_auth.registration.urls')),
    path('user/auth/refresh-token/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('schema/', get_schema_view(
        title='Full Stack Hero',
        description="API for all things …",
        version=__version__
    ), name='openapi-schema'),
]
