from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class CustomPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.view_%(model_name)s'],
        'PUT': ['%(app_label)s.view_%(model_name)s'],
        'PATCH': ['%(app_label)s.view_%(model_name)s'],
        'DELETE': ['%(app_label)s.view_%(model_name)s'],
    }

class PaginationPage(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 1