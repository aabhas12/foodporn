from rest_framework import serializers
from foodshare.models import recipe

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model=recipe
        fields = ('user','title','time','Servings','created_at','updated_at')