from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from recipe.models import Recipe

# Create your tests here.
from recipe.serializers import RecipeSerializer
from user.models import Users


class RecipeTest(TestCase):
    """
        Test case for get of recipe model
    """

    def setUp(self):
        user = Users.objects.create(first_name="1213", last_name="sfdadsdfda")
        Recipe.objects.create(user=user, title="New one for testing", time=321, servings=21,
                              description="sadsasd")
        Recipe.objects.create(user=user, title="New seoncd for testing", time=321, servings=21,
                              description="sadsasd")
        Recipe.objects.create(user=user, title="New ne for testing", time=321, servings=21,
                              description="sadsasd")
        Recipe.objects.create(user=user, title="New on for testing", time=321, servings=21,
                              description="sadsasd")


    def test_get_all_recipes(self):
        response = self.client.get(reverse("get_recipes"))
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_recipe(self):
        response = self.client.get(reverse("recipe", kwargs={'pk': 30 }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




