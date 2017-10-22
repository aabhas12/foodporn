from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from foodshare.serializers import RecipeSerializer,RecipegetSerializer
from rest_framework import status
from foodshare.models import recipe

class Recipe(APIView):
    def get(self,request):
        recipe_all = recipe.objects.all()
        serialize = RecipeSerializer(recipe_all,many=True)
        return Response(serialize.data)

    def post(self,request):
        serialize = RecipeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)


def GetRecipe(request,pk):
    if request.method == 'GET':
        recipe_all = recipe.objects.get(id=pk)
        serialize = RecipegetSerializer(recipe_all)
        return JsonResponse(serialize.data)