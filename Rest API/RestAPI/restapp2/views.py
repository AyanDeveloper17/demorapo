from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView

# Create your views here.
class StudentApi(APIView):

    def get(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'status':200,'message':'data saved successfully','payload':serializer.data})
        

    def put(self,request):
       pass

    def patch(self,request):
        try:
            stud = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(stud,data=request.data,partial=True)
            
            if not serializer.is_valid():
                return Response({'status':403,'message':'something went wrong','error':serializer.errors})

            serializer.save()
            return Response({'status':200,'message':'data has been updated','payload':serializer.data})

        except Exception as e:
            return Response({'status':403,'message':'data does not exist'})
        return Response({'status':200,'message':'data sent securely','payload':serializer.data})

    def delete(self,request):
        stu  = Student.objects.get(id=request.data['id'])
        # stu = Student.objects.get(id=id)
        stu.delete()
        return Response('Data has been deleted successfully')
        





















































# @api_view(['POST'])
# def create(request):
#     try:
#         serializer = StudentSerializer(data=request.data)

#         if not serializer.is_valid():

#             return Response({'status':403,'message':'something went wrong','errors':serializer.errors})


#         serializer.save()
#     except Exception as e:
#         return Response(e)
#     return Response({'status':100,'message':'data has been sent','data':serializer.data})

# @api_view(['GET'])
# def show(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu,many=True)

#     return Response(serializer.data)
    

# @api_view(['DELETE'])
# def delete(request,id):
#     stu=Student.objects.get(id=id)
#     stu.delete()
#     return Response("Data has been deleted successfully")


# @api_view(['PATCH'])
# def update(request,pk):
#     try:

#         stud = Student.objects.get(id=pk)
#         print(stud)
#         serializer = StudentSerializer(stud,data=request.data,partial=True)
#         # # print(serializer)

#         if  serializer.is_valid():
#         #     print(serializer.errors)
#         #     return Response({'status':403,'message':'Data Does not exist','error':serializer.errors})
#             serializer.save()
#             return Response({'status':200,'message':'Data has been sent','data':serializer.data})

#     except Exception as e:
#         print(e)

#     return Response({'status':200,'message':'invalid id'})

# @api_view(['PATCH'])
# def update(request,pk):
#     stu = Student.objects.get(id=pk)
#     serializer = StudentSerializer(stu,data=request.data,partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status':200,'message':'Data has been sent','payload':serializer.data})    
#     else:
#         return Response({'status':403,'message':'something went wrong'})

#     return Response({'status':200,'message':'saved successfully'})

# @api_view(['PATCH'])
# def update_student(request,pk):
#     try:

#         student_obj=Student.objects.get(id=pk)
#         print(student_obj)
#         serializer=StudentSerializer(student_obj,data=request.data,partial=True)

#         if not serializer.is_valid():
#             return Response({'status':403,'message':'Something went wrong','data':serializer.errors})

#         serializer.save()
#         return Response({'status':200,'payload':serializer.data,'message':'you sent'})

#     except Exception as e:
#         print(e)

#         return Response({'status':403,'message':'invalid id'})