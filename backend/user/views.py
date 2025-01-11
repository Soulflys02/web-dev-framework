from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.
class User(APIView):
    def post(self, request):
        serializer: UserSerializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        