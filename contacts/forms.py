from django import forms
from .models import Contact
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone1', 'phone2', 'address']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 1'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number 2'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        }

class ContactSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search contacts...'}))

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
