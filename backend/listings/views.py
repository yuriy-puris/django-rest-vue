from rest_framework import viewsets

# model
from .models import Listings
#serializer
from .serializer import ListingsSerializer
#class
class ListingsViewSet(viewsets.ModelViewSet):
  queryset = Listings.objects.all()
  serializer_class = ListingsSerializer