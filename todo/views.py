from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializers
from .models import Todo


class TodoViewSet(viewsets.ModelViewSet):

    #API endpoint that allows users to be viewed or edited.
    
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializers
    permission_classes = [] #permissions.IsAuthenticated