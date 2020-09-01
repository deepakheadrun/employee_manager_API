from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role, UserRole
from .serializers import RoleSerializer
from rest_framework import permissions

class UserRoleView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        userrole = UserRole.objects.get(userid=request.user)
        role = Role.objects.get(pk=userrole.roleid_id)
        serializer =RoleSerializer(role)
        return Response(serializer.data)
        
