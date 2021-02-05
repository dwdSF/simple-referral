from django import forms

from .models import Code


class CodeForm(forms.ModelForm):
    ''' SMS Code verification form '''

    number = forms.CharField(
        label='', help_text='Enter SMS verification code.',
        widget=forms.TextInput(attrs={'placeholder': 'Example: E3FP0D'}) # noqa
    )

    class Meta:
        model = Code
        fields = ('number',)
