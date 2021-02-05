from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class TestProfile(TestCase):
    ''' Comment here '''

    def setUp(self):
        self.client = Client()
        self.logged_client = Client()
        self.user = User.objects.create_user(
            phone_number='+77777777777'
        )
        self.test_user = User.objects.create_user(
            phone_number='+66666666666'
        )
        self.logged_client.force_login(self.user)

    def test_profile_info(self):
        phone_number = self.user.phone_number
        invite_code = self.user.invite_code
        response = self.logged_client.get(reverse('profile-view'))
        self.assertContains(response, phone_number)
        self.assertContains(response, invite_code)

    def test_code_activation(self):
        wrong_code = 'KKKKKK'
        test_user_code = self.test_user.invite_code

        self.logged_client.post(reverse('invite'), {'invite_code': wrong_code})
        response = self.logged_client.get(reverse('profile-view'))
        self.assertNotContains(response, wrong_code)

        self.logged_client.post(reverse('invite'),
                                {'invite_code': test_user_code})
        response = self.logged_client.get(reverse('profile-view'))
        self.assertContains(response, test_user_code)

    def test_refprofile_info(self):
        test_user_code = self.test_user.invite_code
        test_user_phone = self.test_user.phone_number
        response = self.logged_client.get(reverse('refprofile-view',
                                          args=[test_user_code]))

        self.assertContains(response, test_user_code)
        self.assertContains(response, test_user_phone)
