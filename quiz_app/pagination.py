from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

class Mypagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        context ={
            'status':status.HTTP_200_OK,
            'success':True,
            'response':data,
            'links': {'next': self.get_next_link(),'previous': self.get_previous_link()}
        }
        return Response(context,status=status.HTTP_200_OK)