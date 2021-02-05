from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ReferralForm(forms.Form):
    ''' Form for the user to enter the invite code of another user. '''

    def __init__(self, *args, **kwargs):
        super(ReferralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    invite_code = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Invite code'}) # noqa
    )
