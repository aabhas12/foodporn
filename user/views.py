from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import UsergetSerializer, UsersetSerializer
from rest_framework import status
from user.models import Users
from django.db import transaction

class UserAuth(APIView):
    def get(self, request, pk):
        if Users.objects.filter(social_media_id=pk).exists():
            user = Users.objects.filter(social_media_id=pk)
            serialize = UsergetSerializer(user)
            return Response(data=serialize.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serialize = UsersetSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serialize.data, status=status.HTTP_404_NOT_FOUND)

