from django.db import models

class History(models.Model):
    website = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website