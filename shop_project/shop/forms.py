from django import forms
from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['client', 'amount', 'interest_rate']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['client', 'account_number', 'balance']

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['client', 'status']