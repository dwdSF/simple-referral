from codes.models import Code
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class TestАuthorization(TestCase):
    ''' Health tests of the authorization and verification page '''

    def setUp(self):
        self.client = Client()
        self.logged_client = Client()
        self.user = User.objects.create_user(
            phone_number='+77777777777'
        )
        self.logged_client.force_login(self.user)

    def test_login_page(self):
        text = 'Authorization'
        response = self.client.get(reverse('login-view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text)

    def test_login_redirect(self):
        phone_number = '+77777777777'
        response = self.client.post(reverse('login-view'),
                                    {'phone_number': phone_number})
        self.assertRedirects(response, f'{reverse("verify-view")}',
                             status_code=302)

    def test_verifying(self):
        phone_number = '+77777777777'
        self.client.post(reverse('login-view'),
                         {'phone_number': phone_number})
        user = User.objects.get(phone_number=phone_number)
        sms_code = Code.objects.get(user=user)
        response = self.client.post(reverse('verify-view'),
                                    {'number': sms_code.number})
        self.assertRedirects(response, f'{reverse("profile-view")}',
                             status_code=302)

    def test_auth_to_login(self):
        login_response = self.logged_client.get(reverse('login-view'))
        verify_response = self.logged_client.get(reverse('verify-view'))
        self.assertRedirects(login_response, f'{reverse("profile-view")}',
                             status_code=302)
        self.assertRedirects(verify_response, f'{reverse("profile-view")}',
                             status_code=302)

    def test_noauth_to_profile(self):
        response = self.client.get(reverse('profile-view'))

        self.assertRedirects(
            response,
            f'{reverse("login-view")}?next={reverse("profile-view")}',
            status_code=302
        )
