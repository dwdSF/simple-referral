from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class PhoneAuthBackend(ModelBackend):
    """Phone Authentication Backend.
       Allows user sign in with phone.
    """

    def authenticate(self, request, phone_number=None):
        try:
            user = User.objects.get(phone_number=phone_number)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
