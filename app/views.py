from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.serializers import RecipeSerializer, RecipegetSerializer, IngredientsSerializer, InstructionsSerializer

from rest_framework import status
from app.models import recipe,ingredients,instructions
from django.db import transaction
from rest_framework import mixins
from rest_framework import generics


class Recipe(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = recipe.objects.all()
    serializer_class = RecipegetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    serializer_class = RecipeSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class updaterecipe(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin ,generics.GenericAPIView):
    queryset = recipe.objects.all()
    serializer_class = RecipeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
