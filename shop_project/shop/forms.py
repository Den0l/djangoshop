from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

class RegistrationFrom(UserCreationForm):
    username = forms.CharField(
        label = 'Логин',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label = 'Почта',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label = 'Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Логин',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )