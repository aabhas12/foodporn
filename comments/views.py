from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from drf_openapi.utils import view_config

from comments.Filters import CommentByRecipe, ReplyCommentByComment
from comments.models import Comment, ReplyComment
from comments.serializers import CommentSerializer, ReplyCommentSerializer, GetCommentSerializer
from rest_framework.filters import OrderingFilter


class GetComment(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = GetCommentSerializer
    filter_backends = (CommentByRecipe, OrderingFilter)
    ordering = ('-created_at',)

    @view_config(response_serializer=GetCommentSerializer)
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        return Response(data=response.data, status=response.status_code)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class StoreComment(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (CommentByRecipe, OrderingFilter)
    ordering = ('-created_at',)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return Response(data=response.data, status=response.status_code)


class ReplyCommentStore(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyCommentSerializer
    filter_backends = (ReplyCommentByComment, OrderingFilter)
    ordering = ('created_at',)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


