from enum import Enum, unique

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email: str, name: str, mobile_number: str,
                    whatsapp_number: str, pk_number: int, gender: int,
                    previous_university: str=None, password: str=None):

        if not email or not name or not mobile_number or whastapp_number or pk_number:
            raise ValueError("Users must have required fields")

        user = self.model(
            email=email, name=name, mobile_number=mobile_number, whatsapp_number=whatsapp_number,
            pk_number=pk_number, previous_university=previous_university, gender=gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, name: str, mobile_number: str,
                         whatsapp_number: str, pk_number: int, gender: int,
                         password: str, previous_university: str = None):
        user = self.model(
            email=email, name=name, mobile_number=mobile_number, whatsapp_number=whatsapp_number,
            pk_number=pk_number, previous_university=previous_university, gender=gender
        )
        user.set_password(password)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255, unique=True,
                                     help_text="ex: +6281xxxxxxx")
    whatsapp_number = models.CharField(max_length=255, unique=True,
                                       help_text="ex: +6281xxxxxx")
    pk_number = models.PositiveSmallIntegerField()
    previous_university = models.CharField(max_length=255, blank=True, null=True)

    @unique
    class Gender(Enum):
        MALE = 1
        FEMALE = 2
    gender = models.SmallIntegerField(choices=((g.value, g.name.title()) for g in Gender))

    @unique
    class Type(Enum):
        VOLUNTEER = 1
        INITIATOR = 2
    type = models.SmallIntegerField(choices=((t.value, t.name.title()) for t in Type), default=1)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'mobile_number', 'whatsapp_number', 'pk_number']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    # These 3 method is used for django admin
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
