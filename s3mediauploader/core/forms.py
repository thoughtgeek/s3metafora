from django import forms

from s3mediauploader.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload', )


class UserRegistrationForm(forms.Form):
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,)

