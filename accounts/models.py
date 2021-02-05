from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from .managers import UserManager
from codes.utils import code_generator


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user with phone authentication"""

    phone_regex = RegexValidator(regex=r'^[+]\+?1?\d{9,15}$')
    phone_number = models.CharField(verbose_name='phone number',
                                    validators=[phone_regex],
                                    max_length=17, unique=True)
    invite_code = models.CharField(
        max_length=6, default=code_generator,
        unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_short_name(self):
        return self.phone_number

    def natural_key(self):
        return self.phone_number

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ['-id']
