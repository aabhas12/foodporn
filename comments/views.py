
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from comments.Filters import CommentByRecipe, ReplyCommentByComment
from comments.models import Comment, ReplyComment
from comments.serializers import CommentSerializer, ReplyCommentSerializer
from rest_framework.filters import OrderingFilter


class StoreComment(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GetComment(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (CommentByRecipe, OrderingFilter)
    ordering = ('-created_at',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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


