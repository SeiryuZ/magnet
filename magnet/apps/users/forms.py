from django.contrib.auth.forms import UserCreationForm
from .models import User


class MagnetUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'mobile_number', 'whatsapp_number', 'gender', 'pk_number', 'previous_university'
        )
