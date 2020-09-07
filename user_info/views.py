from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.decorators import action
from .models import Info
from .serializers import InfoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
 
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id']
    # @action(detail=True, methods=['get'])
    # def get_byuser(self, request, user_id=None):
    #     try:
    #         info = Info.objects.get(user_id=user_id)
    #         serializer = InfoSerializer(info)
    #         return Response(serializer.data)
    #     except Info.DoesNotExist:
    #         raise Http404