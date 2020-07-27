from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/', include('api.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippet/', include('snippet.urls')),
    path('login', LoginView.as_view(template_name='fsh/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='fsh/logout.html'), name='logout'),
    path('password', PasswordChangeView.as_view(template_name='fsh/password.html'), name='password'),
    path('admin/', admin.site.urls),

]
