from .models import User
from rest_framework.response import Response
from authh.serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from authh.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update':
            permission_classes = [IsLoggedUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return[permission() for permission in permission_classes]


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(selfself, request):
        content = {'message':'Hello, World'}
        return Response(content)
