from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,viewsets

from .models import InterestedArea
from .serializers import InterestedAreaSerializer


from django_filters.rest_framework import DjangoFilterBackend
class InterestedAreaViewSet(viewsets.ModelViewSet):
    queryset = InterestedArea.objects.all()
    serializer_class = InterestedAreaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id']
