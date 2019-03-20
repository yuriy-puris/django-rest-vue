from rest_framework import serializers

from .models import Listings

class ListingsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Listings
    fields = ('realtors'
              'title', 
              'address', 
              'city', 
              'state', 
              'zipcode', 
              'description', 
              'price', 
              'bedroom'
              'bathrooms'
              'garage'
              'sqft'
              'lot_size'
              'photo_main')