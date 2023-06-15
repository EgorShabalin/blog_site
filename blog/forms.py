from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from blog.models import Post, Comment


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Username"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password"})
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your Password"})
    )


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "img", "category", "posted")

        widgets = {
            "title": forms.TextInput(),
            "text": forms.Textarea(),
            "img": forms.FileInput(),
            "category": forms.Select(),
            "posted": forms.CheckboxInput(),
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "img", "posted")

        widgets = {
            "text": forms.Textarea(),
            "img": forms.FileInput(),
            "posted": forms.CheckboxInput(),
        }
