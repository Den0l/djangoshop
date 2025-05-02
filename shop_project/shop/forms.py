from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']
        widgets = {
            'account': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
            
class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['client', 'amount', 'interest_rate']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['client', 'account_number', 'balance']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['client', 'status']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(
                attrs={'class': 'form-control'}),
        }