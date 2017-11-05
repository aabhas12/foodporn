from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from foodshare.serializers import RecipeSerializer,RecipegetSerializer,IngredientsSerializer,InstructionsSerializer
from rest_framework import status
from foodshare.models import recipe,ingredients,instructions
from django.db import transaction

class Recipe(APIView):
    def get(self,request):
        recipe_all = recipe.objects.all()
        serialize = RecipegetSerializer(recipe_all,many=True)
        return Response(serialize.data)

    def post(self,request):
            serialize = RecipeSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(data=None, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serialize.data, status=status.HTTP_404_NOT_FOUND)

class updaterecipe(APIView):
    def put(self,request,pk):
        recipe_all = recipe.objects.get(id=pk)
        serialize1 = RecipeSerializer(data=request.data)
        if serialize1.is_valid():
            serialize1.update(validated_data=request.data,instance=recipe_all)
            return Response(data=None, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serialize1.data, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        recipe_all = recipe.objects.get(id=pk)
        recipe_all.delete()
        return Response(data=None,status=status.HTTP_200_OK)

    def get(self,request,pk):
        recipe_all = recipe.objects.get(pk=pk)
        serialize = RecipegetSerializer(recipe_all)
        return Response(serialize.data)
