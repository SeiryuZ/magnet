from django.contrib.auth.hashers import check_password

from .models import User


class MobileNumberBackend(object):

    def authenticate(self, username=None, password=None):
        user = User.objects.filter(mobile_number=username).first()
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
