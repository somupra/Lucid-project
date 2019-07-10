from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import url
from users.views import *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mun_dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/', include('api.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
