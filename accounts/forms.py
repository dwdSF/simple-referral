from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(forms.ModelForm):
    ''' Form for authorization by phone '''

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    phone_number = forms.CharField(
        label='',
        help_text='Phone number must be entered in the format: "+999999999".',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}) # noqa
    )

    class Meta:
        model = User
        fields = ('phone_number',)
