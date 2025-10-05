from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attendees.views import AttendeeViewSet

router = DefaultRouter()
router.register(r'attendees', AttendeeViewSet, basename='attendee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # <-- router is under /api/
]


