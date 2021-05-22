from django import forms
from .models import *


class AmountForm(forms.ModelForm):
    class Meta:
        model = Amount
        fields = ['price']