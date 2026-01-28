from django.db import models
from django.contrib.auth.models import User

class EquipmentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    json_stats = models.JSONField()  # This stores the math (averages, etc.)

    class Meta:
        ordering = ['-upload_date'] # Keeps the newest ones on top