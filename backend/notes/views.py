from rest_framework import viewsets

from .models import Note
from .serializer import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all().order_by('-created_at')
  serializer_class = NoteSerializer