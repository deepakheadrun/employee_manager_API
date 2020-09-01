from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from .models import Info
from .serializers import InfoSerializer

class InfoList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InfoDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object_userid(self, user_id):
        try:
            return Info.objects.get(user_id=user_id)
        except Info.DoesNotExist:
            raise Http404
    def get_object_pk(self, pk):
        try:
            return Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        info = self.get_object_userid(id)
        serializer = InfoSerializer(info)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        info = self.get_object_pk(id)
        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)