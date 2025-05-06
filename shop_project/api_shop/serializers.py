from rest_framework import serializers
from shop.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields  = [
            'name',
            'surname',
            'photo',
            'email',
            'phone'
        ]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['client', 'account_number', 'balance']

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ['client', 'amount', 'interest_rate']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['client', 'status', 'applied_at']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'address', 'photo']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'position']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['type', 'price', 'photo']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'cards'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = ['cards', 'order', 'count', 'discount']