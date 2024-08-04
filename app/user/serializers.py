"""
Serializers for the user aPI View
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # the create method is only called when the validation above
    # is successful ie langth is more than 5 foe example
    def create(self,  validate_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validate_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        # instance -> the instance which will be updated
        # validated data -> the data that already passed through
        #                   the serializer validation
        # pop to remove its key from the validated_data dict
        # after retrieving it. not like .get which retrieves only.
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    # the validate method is called by view
    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        # authenticate function comes builtin with django
        # request -> contains the header msg data
        # username -> setting it to the email address
        # password -> password
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
