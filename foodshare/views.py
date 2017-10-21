from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from foodshare.serializers import RecipeSerializer
class Recipe(APIView):
    def get(self,request):

        pass

    def post(self,request):
        serialize = RecipeSerializer(data=request.Data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_404_BAD_REQUEST)


