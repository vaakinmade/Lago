from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            'first_name' : forms.TextInput(attrs = {'placeholder': 'First Name', 'required':'required'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': 'Last Name', 'required':'required'}),
            'email' : forms.TextInput(attrs = {'placeholder': 'Email', 'required':'required'}),
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
        self.fields["username"].label = ""
        self.fields["username"].help_text = "This is how you will be publicly identified"
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = None
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
        #self.fields["username"].widget = forms.HiddenInput(attrs={'value': 'Username'})
		


class AuthenticateForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
       
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    # def authenticate(self, username, password):
    #     print("Got this far2")
    #     if '@' in username:
    #         kwargs = {'email': username}
    #     else:
    #         kwargs = {'username': username}
    #     try:
    #         user = get_user_model().objects.get(**kwargs)
    #         if user.check_password(password):
    #             return user
    #     except User.DoesNotExist:
    #         return None