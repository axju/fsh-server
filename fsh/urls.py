from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.schemas import get_schema_view

from fsh import __version__
from fsh.apps.snippet.views import UserViewSet, InfoView
from fsh.apps.snippet.urls import router as snippet_router

router = routers.DefaultRouter()
router.registry.extend(snippet_router.registry)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('infos/', InfoView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path('admin/', admin.site.urls),

    path('openapi/', get_schema_view(
        title="Full Stack Hero",
        version=__version__
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
