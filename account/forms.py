from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from account.models import User


class register(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'date_of_birth', 'gender')

    def clean_email(self):
        
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already registered")
        return email

    def clean_password2(self):

        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match")
        return password2


class sign(forms.Form):
    email = forms.CharField(label='username')
    password = forms.CharField(label = 'password')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email