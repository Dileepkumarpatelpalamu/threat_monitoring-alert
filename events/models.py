# events/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# events/models.py
class Event(models.Model):
    source = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=20, choices=[('Low','Low'),('Medium','Medium'),('High','High'),('Critical','Critical')])
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# events/models.py
class Alert(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Open','Open'),('Acknowledged','Acknowledged'),('Resolved','Resolved')], default='Open')
    created_at = models.DateTimeField(auto_now_add=True)