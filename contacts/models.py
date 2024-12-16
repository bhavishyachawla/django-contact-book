from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # optional field
    last_name = models.CharField(max_length=100, blank=True, null=True)  # non-nullable field, with a default value
    email = models.EmailField()
    phone1 = models.CharField(max_length=15)  # renamed from 'phone'
    phone2 = models.CharField(max_length=15, blank=True, default='')  # optional field
    address = models.TextField(blank=True, null=True)  # optional field with default value
    

    class Meta:
        indexes = [
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone1']),
            models.Index(fields=['phone2']),
            models.Index(fields=['address']),
        ]

    def full_name(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()
    

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
