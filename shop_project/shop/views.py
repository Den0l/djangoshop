from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models  import *
from .forms  import *

def base_view(request):
    return render(request, 'base.html')

def about_view(request):
    return render(request, 'about.html')

def all_products_view(request):
    return render(request, 'all_products.html')

def cart_view(request):
    return render(request, 'cart.html')

def categories_view(request):
    return render(request, 'categories.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def how_to_find_view(request):
    return render(request, 'how_to_find.html')

def index_view(request):
    return render(request, 'index.html')

def privacy_view(request):
    return render(request, 'privacy.html')

def product_detail_view(request):
    return render(request, 'product_detail.html')


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('client-list')

class AccountListView(ListView):
    model = Account
    template_name = 'account/account_list.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'account/account_detail.html'
    context_object_name = 'account'

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm 
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-list')

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account/account_delete.html'
    success_url = reverse_lazy('account-list')

class CreditListView(ListView):
    model = Credit
    template_name = 'credit/credit_list.html'
    context_object_name = 'credits'

class CreditDetailView(DetailView):
    model = Credit
    template_name = 'credit/credit_detail.html'
    context_object_name = 'credit'

class CreditCreateView(CreateView):
    model = Credit
    form_class = CreditForm 
    template_name = 'credit/credit_form.html'
    success_url = reverse_lazy('credit-list')

class CreditUpdateView(UpdateView):
    model = Credit
    form_class = CreditForm
    template_name = 'credit/credit_form.html'
    success_url = reverse_lazy('credit-list')

class CreditDeleteView(DeleteView):
    model = Credit
    template_name = 'credit/credit_delete.html'
    success_url = reverse_lazy('credit-list')

class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction/transaction_list.html'
    context_object_name = 'transactions'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/transaction_detail.html'
    context_object_name = 'transaction'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm 
    template_name = 'transaction/transaction_form.html'
    success_url = reverse_lazy('transaction-list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction/transaction_form.html'
    success_url = reverse_lazy('transaction-list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transaction/transaction_delete.html'
    success_url = reverse_lazy('transaction-list')

class LoanApplicationListView(ListView):
    model = LoanApplication
    template_name = 'loan_application/loan_application_list.html'
    context_object_name = 'loan_applications'

class LoanApplicationDetailView(DetailView):
    model = LoanApplication
    template_name = 'loan_application/loan_application_detail.html'
    context_object_name = 'loan_application'

class LoanApplicationCreateView(CreateView):
    model = LoanApplication
    form_class = LoanApplicationForm
    template_name = 'loan_application/loan_application_form.html'
    success_url = reverse_lazy('loan-application-list')

class LoanApplicationUpdateView(UpdateView):
    model = LoanApplication
    form_class = LoanApplicationForm 
    template_name = 'loan_application/loan_application_form.html'
    success_url = reverse_lazy('loan-application-list')

class LoanApplicationDeleteView(DeleteView):
    model = LoanApplication
    template_name = 'loan_application/loan_application_delete.html'
    success_url = reverse_lazy('loan-application-list')