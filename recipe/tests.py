from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

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
        self.first_recipe = Recipe.objects.create(user=user, title="New one for testing", time=321, servings=21,
                              description="sadsasd")
        self.valid_payload = {
          "user": 1,
          "title": "Pannssbdar",
          "time": 321,
          "servings": 311,
          "description":"aadasda",
          "recipe_video": [
            {
              "video": None
            }
          ],
          "recipes_ingredients": [
            {
              "ingredient": "Jeezzfff111ffzra",
              "quantity": "1221"
            },
            {
              "ingredient": "Jeera",
              "quantity": "121"
            },
            {
              "ingredient": "Jeera",
              "quantity": "112121"
            }
          ],
          "recipes_instructions": [
            {
              "step": "sdsDSD"
            },
            {
              "step": "sdsDSD"
            },
            {
              "step": "sdsDSD"
            }
          ]

        }
        self.invalid_payload = {
            "user": 12,
            "title": "Pannssbdar",
            "time": 321,
            "servings": 311,
            "description": "aadasda",
            "recipe_video": [
                {
                    "video": None
                }
            ],
            "recipes_ingredients": [
                {
                    "ingredient": "Jeezzfff111ffzra",
                    "quantity": "1221"
                },
                {
                    "ingredient": "Jeera",
                    "quantity": "121"
                },
                {
                    "ingredient": "Jeera",
                    "quantity": "112121"
                }
            ],
            "recipes_instructions": [
                {
                    "step": "sdsDSD"
                },
                {
                    "step": "sdsDSD"
                },
                {
                    "step": "sdsDSD"
                }
            ]

        }

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

    def test_get_valid_recipe(self):
        response = self.client.get(reverse("recipe", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_recipe(self):
        response = self.client.post(reverse("get_recipes"), data=json.dumps(self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_recipe(self):
        response = self.client.post(reverse("get_recipes"), data=json.dumps(self.invalid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_puppy(self):
        response = self.client.patch(
            reverse('recipe', kwargs={'pk': self.first_recipe.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_puppy(self):
        response = self.client.patch(
            reverse('recipe', kwargs={'pk': self.first_recipe.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_recipe(self):
        response = self.client.delete(
            reverse('recipe', kwargs={'pk': self.first_recipe.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






