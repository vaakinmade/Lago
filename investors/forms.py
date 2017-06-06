from django import forms
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


class FundForm(forms.ModelForm):
	class Meta:
		model = models.Wallet
		fields = ('amount', 'activity')

		widgets = {
            'activity': forms.Textarea(attrs={'rows': 1, 'required':True}),
            'amount': forms.TextInput(attrs={'required':True}),
        }

class PasswordChangeForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput())
	new_password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())

	def __init__(self, request, *args, **kwargs): 
		super(PasswordChangeForm, self).__init__(*args, **kwargs)
		self.request = request
   
	def clean(self):
		cleaned_data = super(PasswordChangeForm, self).clean()
		password = cleaned_data.get("password")
		new_password = cleaned_data.get("new_password")
		confirm_password = cleaned_data.get("confirm_password")
		if password and new_password and confirm_password:
			if new_password != confirm_password:
				raise forms.ValidationError(
					"Password Inconsistency.")
			else:
				user = authenticate(username=self.request.user, password=password)
				if user is not None:
					user.set_password(new_password)
					user.save()
					update_session_auth_hash(self.request, user)
					messages.add_message(self.request, messages.SUCCESS,
					     "Password changed")
				else:
					raise forms.ValidationError(
						"Incorrect Password.")
