from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from .models import Skill
from .serializers import SkillSerializer

class SkillList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillDetail(APIView):
    # permission_classes = [IsAuthenticated]
    def get_object_userid(self, user_id):
        try:
            return Skill.objects.filter(user_id=user_id)
        except Skill.DoesNotExist:
            raise Http404
    def get_object_pk(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        skill = self.get_object_userid(id)
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        skill = self.get_object_pk(id)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        skill = self.get_object_pk(id)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)