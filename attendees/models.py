from django.db import models

class Attendee(models.Model):
    #Basic info
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=128, blank=True)

    # Demographics
    date_of_birth   = models.DateField(blank=True, null=True)
    country         = models.CharField(max_length=100, blank=True)
    state           = models.CharField(max_length=100, blank=True)
    gender_identity = models.JSONField(default=list, blank=True) 
    gender_other    = models.CharField(max_length=100, blank=True)
    race_ethnicity  = models.CharField(max_length=100, blank=True)
    race_other      = models.CharField(max_length=100, blank=True)

    # Academic info
    level_of_study  = models.CharField(max_length=100, blank=True)
    year_level      = models.CharField(max_length=100, blank=True)
    study_other     = models.CharField(max_length=100, blank=True)
    field_of_study  = models.CharField(max_length=255, blank=True)
    field_other     = models.CharField(max_length=100, blank=True)
    school          = models.CharField(max_length=255, blank=True)
    school_other    = models.CharField(max_length=100, blank=True)
    panther_id      = models.CharField(max_length=50, blank=True)

    # Social
    linkedin    = models.URLField(blank=True)
    github      = models.URLField(blank=True)
    website     = models.URLField(blank=True)
    discord     = models.CharField(max_length=100, blank=True)

    # Additional info
    food_allergies  = models.JSONField(default=list, blank=True)
    shirt_size      = models.CharField(max_length=5, blank=True)

    # Agreements
    code_of_conduct     = models.BooleanField(default=False)
    photography_consent = models.BooleanField(default=False)

    # Files and tracking
    resume      = models.FileField(upload_to="resumes/", blank=True, null=True)
    checked_in  = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
