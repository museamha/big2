from django.urls import path
from . import views
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test API for my Django app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/comments/', views.FieldAPI.as_view(), name='comment-create'),
    path("", views.FildsViews.as_view(), name="bott"),
    path('api/comments/', views.FieldAPI.as_view(), name='comment-api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  
]
