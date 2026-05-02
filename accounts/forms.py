from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input-field",
        "placeholder": "Create password"
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input-field",
        "placeholder": "Confirm password"
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "input-field",
                "placeholder": "Email address"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input-field",
        "placeholder": "Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input-field",
        "placeholder": "Password"
    }))


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={
        "class": "input-field text-center tracking-widest",
        "placeholder": "Enter OTP"
    }))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "location", "website", "tags", "profession"]
        widgets = {
            "bio": forms.Textarea(attrs={
                "class": "input-field",
                "rows": 4,
                "placeholder": "Write something about yourself"
            }),
            "location": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Location"
            }),
            "website": forms.URLInput(attrs={
                "class": "input-field",
                "placeholder": "Website URL"
            }),
            "tags": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Django, Python, AI, Design"
            }),
            "profession": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Profession"
            }),
        }