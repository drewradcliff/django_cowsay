from django import forms
from homepage.models import Input


class AddTextForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ["text"]