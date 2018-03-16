from rest_framework.filters import BaseFilterBackend


class CommentByRecipe(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(recipe__id=int(request.query_params['recipe_id']))


class ReplyCommentByComment(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(comment__id=int(request.query_params['comment_id']))