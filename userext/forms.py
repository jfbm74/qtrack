from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un usuario con este email ya existe.")
        return email

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'bio')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise forms.ValidationError("El número de teléfono debe contener solo dígitos.")
        return phone_number
