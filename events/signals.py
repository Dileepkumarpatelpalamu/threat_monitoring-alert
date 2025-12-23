# events/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event, Alert

@receiver(post_save, sender=Event)
def create_alert(sender, instance, created, **kwargs):
    if created and instance.severity in ['High','Critical']:
        Alert.objects.create(event=instance)