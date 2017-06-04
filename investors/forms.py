from django import forms
from . import models

class FundForm(forms.ModelForm):
	class Meta:
		model = models.Wallet
		fields = ('amount', 'activity')

		widgets = {
            'activity': forms.Textarea(attrs={'rows': 1, 'required':True}),
            'amount': forms.TextInput(attrs={'required':True}),
        }


class WithdrawalForm(FundForm):
	pass
   