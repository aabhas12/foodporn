from rest_framework import serializers
from app.models import Recipe, Instructions, Ingredients, RecipeVideo, Comment , ReplyComment



class InstructionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructions
        fields = 'step',


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('quantity','ingredient')


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeVideo
        fields = 'video',

class ReplyCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReplyComment
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.reply = validated_data['reply']
        instance.save()


class CommentSerializer(serializers.ModelSerializer):
    reply_comment = ReplyCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'likes', 'reply_comment')


class RecipeSerializer(serializers.ModelSerializer):
    recipes_instructions = InstructionsSerializer(many=True)
    recipes_ingredients = IngredientsSerializer(many=True)
    recipe_video = VideoSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('user','title','time','servings','recipes_instructions','recipes_ingredients', 'recipe_video')

    def create(self, validated_data):
        recipes_ingredients = validated_data.pop('recipes_ingredients')
        recipes_instructons = validated_data.pop('recipes_instructions')
        recipe_video = validated_data.pop('recipe_video')
        recipe1 = Recipe.objects.create(**validated_data)
        for video in recipe_video:
            RecipeVideo.objects.create(recipe=recipe1, **video)
        for recipe2 in recipes_ingredients:
            Ingredients.objects.create(recipe=recipe1, **recipe2)
        for recipe3 in recipes_instructons:
            Instructions.objects.create(recipe=recipe1, **recipe3)
        return recipe1

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.time = validated_data['time']
        instance.Servings = validated_data['servings']
        recipes_ingredients = validated_data['recipes_ingredients']
        recipes_instructons = validated_data['recipes_instructions']
        instance.save()
        ingredient = (instance.recipes_ingredients).all()
        ingredient.delete()
        instruction = (instance.recipes_instructions).all()
        instruction.delete()
        for recipe2 in recipes_ingredients:
            Ingredients.objects.create(recipe=instance, **recipe2)
        for recipe3 in recipes_instructons:
            Instructions.objects.create(recipe=instance, **recipe3)
        return instance





