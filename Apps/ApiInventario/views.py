from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActivoSerializer
from .models import Activo
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ActivoViewSet(viewsets.ModelViewSet):
    serializer_class = ActivoSerializer
    queryset = Activo.objects.all()
    permission_classes = [IsAuthenticated]