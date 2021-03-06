from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserChangeAdminForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'gender', 'mobile_number', 'whatsapp_number', 'pk_number',
                  'previous_university', 'type', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeAdminForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'pk_number', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('gender', 'mobile_number', 'whatsapp_number',
                       'pk_number', 'previous_university')
        }),
        ('Permissions', {'fields': ('is_active', 'is_admin',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute  when creating a user.
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'name', 'gender', 'mobile_number', 'whatsapp_number', 'pk_number',
                           'previous_university', 'password1', 'password2')
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new
# UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using
# Django's built-in permissions,
# unregister the Group model
# from admin.
admin.site.unregister(Group)
