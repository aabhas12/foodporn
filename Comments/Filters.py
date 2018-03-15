from rest_framework.filters import BaseFilterBackend


class CommentByRecipe(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(recipe__id=int(view.kwargs['pk']))
