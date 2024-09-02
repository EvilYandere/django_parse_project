from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from logs.views import LogEntryViewSet

router = DefaultRouter()
router.register(r'logs', LogEntryViewSet)

urlpatterns = [  # добавлены пути до админки и API
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
