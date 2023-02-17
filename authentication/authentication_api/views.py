from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from authentication.authentication_api.serializer import (
    UserRegisterSerializer,
)


class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            get_data = request.data
            serializer = UserRegisterSerializer(data=get_data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    "status": status.HTTP_200_OK,
                    "success":True,
                    "response":"User Created Successfully"
                }
                return Response(context,status=status.HTTP_200_OK)

            else:
                context = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":serializer.errors
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as exception:
            context = {
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "response": str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            get_username = request.POST.get('username',None)
            get_password = request.POST.get('password',None)

            authenticate_user = authenticate(username=get_username, password=get_password)
            if authenticate_user is not None:
                login(request,authenticate_user)
                context = {
                    "status":status.HTTP_200_OK,
                    "success": True,
                    "response": "Logged in successfully"
                }
                return Response(context,status=status.HTTP_200_OK)

            else:
                context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response": "Invalid username or password"
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success": False,
                "response": str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)






