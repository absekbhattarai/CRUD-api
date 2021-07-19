#Main URLs
from django.contrib import admin
from django.urls import path,include
from book_management.views import bookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Book CRUD API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@bookcrud.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = DefaultRouter()
router.register(r'book', bookViewSet, basename='book list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
