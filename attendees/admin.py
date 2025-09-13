from django.contrib import admin
from .models import Attendee

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "school", "checked_in", "created_at")
    search_fields = ("first_name", "last_name", "email", "school")