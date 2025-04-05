from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class News(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('entertainment', 'Entertainment'),
        ('share_market', 'Share Market'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return self.title
