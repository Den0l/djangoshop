from rest_framework import routers
from .views import *

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet, basename="accounts")
router.register('credits', CreditViewSet, basename="credits")
router.register('transactions', TransactionViewSet, basename="transactions")
router.register('loan-applications', LoanApplicationViewSet, basename="loan-applications")
router.register('branches', BranchViewSet, basename="branches")
router.register('employees', EmployeeViewSet, basename="employees")
router.register('cards', CardViewSet, basename="cards")
router.register('orders', OrderViewSet, basename="orders")
router.register('pos-orders', PosOrderViewSet, basename="pos-orders")

urlpatterns += router.urls