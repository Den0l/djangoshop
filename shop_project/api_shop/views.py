from rest_framework import viewsets
from .permission import *
from shop.models import *
from .serializers import *

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class LoanApplicationViewSet(viewsets.ModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage