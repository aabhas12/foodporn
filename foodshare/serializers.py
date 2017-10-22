from rest_framework import serializers
from foodshare.models import recipe
import datetime

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model=recipe
        fields = ('user','title','time','Servings')


class RecipegetSerializer(serializers.ModelSerializer):

    class Meta:
        model=recipe
        fields = "__all__"



