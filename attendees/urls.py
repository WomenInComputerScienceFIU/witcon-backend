from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attendees.views import AttendeeViewSet

router = DefaultRouter()
router.register(r'attendees', AttendeeViewSet, basename='attendee')

urlpatterns = [
    path("api/", include(router.urls)),
]

