from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Code

User = get_user_model()


class TestCodeActions(TestCase):
    ''' Test for changing the SMS code after each authorization '''

    def setUp(self):
        self.client = Client()

    def test_code_changing(self):
        phone_number = '+77777777777'
        self.client.post(reverse('login-view'),
                         {'phone_number': phone_number})
        user = User.objects.get(phone_number=phone_number)
        sms_code = Code.objects.get(user=user)
        self.client.post(reverse('verify-view'),
                         {'number': sms_code.number})
        new_sms_code = Code.objects.get(user=user)

        self.assertNotEqual(sms_code.number, new_sms_code.number)
