from .models import Todo
from rest_framework import serializers

#This build an endpoint for the API to access the data
class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'created_at']