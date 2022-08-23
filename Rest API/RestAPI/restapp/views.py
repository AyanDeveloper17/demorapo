from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task


@api_view(['GET'])
# Create your views here.
def apiview(request):
    api_url={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update ':'/task-update/<str:pk>/',
        'Delete ':'/task-delete/<str:pk>/',
    }
    return Response(api_url)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def taskdetails(request,pk):
    task = Task.objects.get(id=pk)

    serializer = TaskSerializer(task,many=False)

    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['POST'])
def taskupdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response()
    

@api_view(['DELETE'])
def taskdelete(request,pk):
    dlt=Task.objects.get(id=pk)
    dlt.delete()

    return Response('User has been deleted successfully')


