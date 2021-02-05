from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Code

User = get_user_model()


@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    ''' A signal to resave the user after authorization.
    Needed to generate new code. '''

    if created:
        Code.objects.create(user=instance)
