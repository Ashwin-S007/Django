from django import forms
from .models import DiabetesInput

class Diabetes_form(forms.ModelForm):
    class Meta:
        model=DiabetesInput
        fields='__all__'