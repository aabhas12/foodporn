from rest_framework import serializers
from foodshare.models import recipe,instructions,ingredients
import datetime



class InstructionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = instructions
        fields = 'step',

class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model=ingredients
        fields = ('quantity','ingredient')

class RecipeSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsSerializer(many=True)
    class Meta:
        model=recipe
        fields = ('user','title','time','Servings','recipes_instructions','recipes_ingredients')

    def create(self, validated_data):
        print(validated_data)
        recipes_ingredients = validated_data.pop('recipes_ingredients')
        recipes_instructons = validated_data.pop('recipes_instructions')
        recipe1 = recipe.objects.create(**validated_data)
        for recipe2 in recipes_ingredients:
            ingredients.objects.create(recipe=recipe1, **recipe2)
        for recipe3 in recipes_instructons:
            instructions.objects.create(recipe=recipe1, **recipe3)
        return recipe1

    def update(self, instance, validated_data):
        print(validated_data)
        instance.title = validated_data['title']
        instance.time = validated_data['time']
        instance.save()
        # recipes_ingredients = validated_data.pop('recipes_ingredients')
        # recipes_instructons = validated_data.pop('recipes_instructions')
        # recipe1 = recipe.objects.create(**validated_data)
        # for recipe2 in recipes_ingredients:
        #     ingredients.objects.create(recipe=recipe1, **recipe2)
        # for recipe3 in recipes_instructons:
        #     instructions.objects.create(recipe=recipe1, **recipe3)
        return instance

class RecipegetSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsSerializer(many=True)
    class Meta:
        model=recipe
        fields = "__all__"



