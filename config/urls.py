
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view=get_schema_view(
    openapi.Info(
        title='Book lis api',
        default_version='v1',
        discription='Library demo project',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='raxmatjonhamidov242@gmail.com'),
        license=openapi.License(name='demo license'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/v1/',include("books.urls")),

    #swagger
    path('',scheme_view.with_ui(
        'swagger',cache_timeout=0), name='swagger-swagger-ui'),
   # redoc
    path('redoc/',scheme_view.with_ui(
        'redoc',cache_timeout=0), name='scheme-redoc'),

   #authentication

    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration',include('dj_rest_auth.registration.urls'))

]
