from django.db import models

class Attendee(models.Model):
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    email       = models.EmailField(unique=True)
    school      = models.CharField(max_length=255, blank=True)
    resume      = models.FileField(upload_to="resumes/", blank=True, null=True)
    checked_in  = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
