from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, default="N/A")
    location = models.CharField(max_length=100, default="Unknown")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
