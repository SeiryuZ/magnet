from django.contrib.auth.hashers import check_password
from django.db.models import Q

from .models import User


class MagnetBackend(object):

    def authenticate(self, username=None, password=None):
        user = User.objects.filter(Q(mobile_number=username) | Q(email=username)).first()
        if user:
            valid = check_password(password, user.password)
            if valid:
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
