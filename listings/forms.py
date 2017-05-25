from django import forms

from . import models


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = models.Investment
        fields = [
            'unit_shares',
            'unit_price',
            'investment_cost',
            'transaction_cost',
            'total_cost',
        ]

        widgets = {
            'unit_shares' : forms.HiddenInput(),
            'unit_price' : forms.HiddenInput(),
            'investment_cost' : forms.HiddenInput(),
            'transaction_cost' : forms.HiddenInput(),
            'total_cost' : forms.HiddenInput(),
        }
