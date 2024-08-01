"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from . import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    # Here we basically customize the field sets variables
    # And we have only specified fields that exist in our models
    # and exluded fields which do not exist in the default one such as the username field
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # wide is enabling a css class which beautify the view a little bit
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


# Here we basically register the User model with the specification we specified in our UserAdmin class
admin.site.register(models.User, UserAdmin)
