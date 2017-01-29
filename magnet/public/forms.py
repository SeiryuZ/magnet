from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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


class PasswordChangeForm(DjangoPasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
