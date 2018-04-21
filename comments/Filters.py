from rest_framework.filters import BaseFilterBackend


class CommentByRecipe(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        if 'recipe_in' in request.GET and int(request.GET['recipe_id']):
            return queryset.filter(recipe__id=int(request.GET['recipe_id']))
        else:
            return queryset


class ReplyCommentByComment(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        if 'comment_id' in request.GET and int(request.GET['comment_id']):
            return queryset.filter(comment__id=int(request.GET['comment_id']))
        else:
            return queryset