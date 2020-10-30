from rest_framework import viewsets
from .models import Slot
from .serializers import SlotSerializer

class SlotView(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


