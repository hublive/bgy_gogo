from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

# Create your views here.

@extend_schema(tags=['monitor'])
class MonitorViewSet(viewsets.ViewSet):
    """监控视图集"""
    permission_classes = [IsAuthenticated]
