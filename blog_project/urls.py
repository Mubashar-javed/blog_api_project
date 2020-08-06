from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'

# adding this to generate differenct types of docs generation
schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE, default_version='v1', description=API_DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),

    path('api/v1/rest-auth/registration',
         include('rest_auth.registration.urls')),

    path('api-auth/', include('rest_framework.urls')),

    # docs routes
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),


    re_path(r'swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
]
