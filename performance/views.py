from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        performance = Performance.objects.all()
        serializer = PerformanceSerializer(performance, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PerformanceDetail(APIView):
    # permission_classes = [IsAuthenticated]
    def get_object_userid(self, user_id):
        try:
            return Performance.objects.filter(user_id=user_id).order_by('-id')[:10]
        except Performance.DoesNotExist:
            raise Http404
    def get_object_pk(self, pk):
        try:
            return Performance.objects.get(pk=pk)
        except Performance.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        performance = self.get_object_userid(id)
        serializer = PerformanceSerializer(performance, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        performance = self.get_object_pk(id)
        serializer = PerformanceSerializer(performance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        performance = self.get_object_pk(id)
        performance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)