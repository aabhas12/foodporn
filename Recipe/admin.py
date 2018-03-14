from django.contrib import admin

# Register your models here.
from Recipe.models import Recipe, Ingredients

admin.site.register(Recipe)
admin.site.register(Ingredients)

