from rest_framework import serializers
from .models import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

        # file size validation
        def validate_resume(self, value):
            if value and value.size > 5 * 1024 * 1024:
                raise serializers.ValidationError("Resume size must be <= 5 MB")
            return value