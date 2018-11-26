from django import forms

from s3mediauploader.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload', )
