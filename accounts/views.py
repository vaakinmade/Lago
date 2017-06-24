from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from . import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import urllib
import json


class LoginView(generic.FormView):
    form_class = forms.AuthenticateForm
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class EmailOrUsernameModelBackend(object):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
    msg = ''

    def form_valid(self, form):
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.self.request.Request(url, data=data)
        response = urllib.self.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success'] is False:
            messages.add_message(self.request, messages.ERROR,
                         "Invalid reCAPTCHA. Please try again.")
            return HttpResponseRedirect(reverse('accounts:signup'))

        SignUp.msg = "Sign up successful. Login with your username/email and password."
        return super(SignUp, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['msg'] = SignUp.msg
        return context
