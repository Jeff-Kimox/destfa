from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User, Sermon, Event


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
        


class SermonForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs = {'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Sermon
        fields = ['title', 'content', 'sermon_from', 'thumbnail', 'featured', 'categories']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'time', 'overview', 'categories', 'featured',
        'thumbnail']

# class JoinUsForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = '__all__'