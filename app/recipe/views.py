"""
Views for recipe APIs.
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeSerializer
    # Represents the objects that are available for this view set.
    # Because it is a ModelViewSet so it expects to work with a model.
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Now we can leave the class as this and be able to perform
    # all of the actions that we need like get, post, etc.
    # However, we need to make sure the get method filters the returned
    # objects with that authenticated user. In order to do this we override
    # the get method.

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')