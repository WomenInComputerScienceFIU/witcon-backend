from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Attendee
from .serializers import AttendeeSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all().order_by("-created_at")
    serializer_class = AttendeeSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "email", "school"]


router = DefaultRouter()
router.register(r'attendees', AttendeeViewSet, basename='attendee')  

# from django.shortcuts import render
# from rest_framework import viewsets, filters
# from .models import Attendee
# from .serializers import AttendeeSerializer

# class AttendeeViewSet(viewsets.ModelViewSet):
#     queryset = Attendee.objects.all().order_by("-created_at")
#     serializer_class = AttendeeSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ["first_name", "last_name", "email", "school"]

