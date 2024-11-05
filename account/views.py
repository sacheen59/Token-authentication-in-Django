from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from account.models import Information
from account.serializers import InformationSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from account.serializers import UserRegistrationSerializer

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class InformationView(ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated,]


class UserRegistrationView(APIView):
    
    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username":user.username,
                "email":user.email,
                "token":user.token
            },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

