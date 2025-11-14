from django import forms
from django.forms import ModelForm, ValidationError
import re

from .models import UserContact


class UserContactForm(ModelForm):
    class Meta:
        model = UserContact
        exclude = ['replied', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite seu email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Digite sua mensagem'
            })
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = re.sub(r'\D', '', phone)
        if len(phone) < 10:
            raise ValidationError('O número deve ter ao menos 10 dígitos.')
        return phone
    
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()