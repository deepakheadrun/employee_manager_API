from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from .models import Comment
from .serializers import CommentSerializer

class CommentList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetail(APIView):
    # permission_classes = [IsAuthenticated]
    def get_object_userid(self, user_id):
        try:
            return Comment.objects.filter(user_id=user_id)
        except Comment.DoesNotExist:
            raise Http404
    def get_object_pk(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        comment = self.get_object_userid(id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        comment = self.get_object_pk(id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        comment = self.get_object_pk(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)