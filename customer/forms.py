from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken. Please choose a different username.")
        return username

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        # Add your custom validation logic for mobile number field
        # Example: Ensure the mobile number is 10 digits long and consists of only numbers
        if len(mobile) != 10 or not mobile.isdigit():
            raise forms.ValidationError("Invalid mobile number.")
        return mobile

