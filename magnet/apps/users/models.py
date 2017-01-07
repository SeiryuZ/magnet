from enum import Enum, unique

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)

    @unique
    class Gender(Enum):
        MALE = 1
        FEMALE = 2
    gender = models.SmallIntegerField(choices=(
        (g.value, g.name.title())for g in Gender)
    )

    is_active = models.BooleanField()



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'nane', 'mobile_number', 'gender']


    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name


