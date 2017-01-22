from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Email or Mobile"),
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(widget=forms.PasswordInput, label=_("Password"))

    error_messages = {
        'invalid_login': _(
            "Wrong username or password."
        ),
        'inactive': _("This account is inactive. Please contact us for assistance."),
    }
