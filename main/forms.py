from django import forms
from django.core.exceptions import ValidationError

from .models import Greeting


class GreetingForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        if Greeting.objects.filter(name=name).exists():
            raise ValidationError(name)
        return name

    class Meta:
        model = Greeting
        fields = (
            'name',
            'last_name',
            'email'
        )


