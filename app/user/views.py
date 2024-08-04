"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    # we are specifying the view to use the custom serializer we made
    # which uses email and password instead of default of username and pass
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    # retrieve -> get method
    # update -> put and patch methods
    serializer_class = UserSerializer
    # type of authentication
    authentication_classes = [authentication.TokenAuthentication]
    # user must be authenticated to use this API
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        # when a user is authenticated, the user object that is beind
        # authenticated gets assigned to the request object that is
        # available in the view
        return self.request.user
