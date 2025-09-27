from rest_framework import serializers
from .models import Attendee
from django.core.validators import URLValidator

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    # Validate resume file size
    def validate_resume(self, value):
        if value and value.size > 5 * 1024 * 1024:  # 5 MB limit
            raise serializers.ValidationError("Resume size must be <= 5 MB")
        return value

    # Optional: ensure URLs are valid if provided
    def validate_linkedin(self, value):
        if value:
            URLValidator()(value)
        return value

    def validate_github(self, value):
        if value:
            URLValidator()(value)
        return value

    def validate_website(self, value):
        if value:
            URLValidator()(value)
        return value

    def validate_gender_identity(self, value):
        """Ensure gender_identity is a list of valid options."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Gender identity must be a list")
        allowed = [choice[0] for choice in self.Meta.model.GENDER_OPTIONS]
        for item in value:
            if item not in allowed and item != self.initial_data.get("gender_other", ""):
                raise serializers.ValidationError(f"Invalid gender identity: {item}")
        return value

    def validate_food_allergies(self, value):
        """Ensure food_allergies is a list of valid options."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Food allergies must be a list")
        allowed = [choice[0] for choice in self.Meta.model.ALLERGIES]
        for item in value:
            if item not in allowed:
                raise serializers.ValidationError(f"Invalid food allergy: {item}")
        return value

    # Optional: hash the password if needed
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        attendee = Attendee(**validated_data)
        if password:
            # simple hashing example; replace with Django auth if needed
            import hashlib
            attendee.password = hashlib.sha256(password.encode()).hexdigest()
        attendee.save()
        return attendee
    
    def validate(self, attrs):
        # Ensure email confirmation is correct if passed
        if 'email' in attrs and self.context.get('request'):
            request_data = self.context['request'].data
            confirm_email = request_data.get('confirmEmail')
            if confirm_email and confirm_email != attrs['email']:
                raise serializers.ValidationError({"confirmEmail": "Emails do not match"})
        return attrs