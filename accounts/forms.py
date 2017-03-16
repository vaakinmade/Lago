from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        model = get_user_model()

        labels = {
            'first_name': _('First Name'),
        }
        
        error_messages = {
            'first_name': {
                'max_length': _("This writer's name is too long."),
            },
        }

        widgets = {
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': 'Last Name'}),
            'email' : forms.TextInput(attrs = {'placeholder': 'Email'}),
            'username' : forms.HiddenInput(attrs = {'value': 'Username2'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
        #self.fields["username"].widget = forms.HiddenInput(attrs={'value': 'Username'})
		