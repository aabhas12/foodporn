
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, filters

from Comments.Filters import CommentByRecipe
from Comments.models import Comment, ReplyComment
from Comments.serializers import CommentSerializer, ReplyCommentSerializer


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
    filter_backends = (CommentByRecipe,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ReplyCommentStore(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyCommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


