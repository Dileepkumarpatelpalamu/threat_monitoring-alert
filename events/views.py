# events/views.py
from rest_framework import viewsets
from .models import Event, Alert
from .serializers import EventSerializer, AlertSerializer
from .permissions import IsAdmin  
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]
    def get_queryset(self):
        qs = super().get_queryset()
        severity = self.request.query_params.get('severity')
        status = self.request.query_params.get('status')
        if severity:
            qs = qs.filter(event__severity=severity)
        if status:
            qs = qs.filter(status=status)
        return qs
