#Main URLs
from django.contrib import admin
from django.urls import path,include
from book_management.views import bookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', bookViewSet, basename='book list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
