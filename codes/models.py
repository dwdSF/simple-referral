from django.db import models
from django.contrib.auth import get_user_model

from.utils import code_generator


User = get_user_model()


class Code(models.Model):
    ''' A model that generates codes to send to users and validate them.
    Works with django-signals. '''

    number = models.CharField(max_length=6, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        code_string = code_generator()
        self.number = code_string

        super().save(*args, **kwargs)
