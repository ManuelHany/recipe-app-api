"""
URL mappings for the recipe app.
"""
from django.urls import (
    path, # define path
    include, # include url using their url name
)

# you can use this default router with an api view to automatically create
# routes for all the different options available for that view.
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]