from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.serializers import RecipeSerializer, IngredientsSerializer, InstructionsSerializer, CommentSerializer, ReplyCommentSerializer

from rest_framework import status
from app.models import Recipe, Ingredients, Instructions, Comment, ReplyComment
from django.db import transaction
from rest_framework import mixins
from rest_framework import generics

class UpdateRecipe(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StoreComment(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ReplyCommentStore(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyCommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
