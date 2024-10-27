from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
