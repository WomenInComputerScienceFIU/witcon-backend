from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Attendee
from .serializers import AttendeeSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all().order_by("-created_at")
    serializer_class = AttendeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "email", "school"]

