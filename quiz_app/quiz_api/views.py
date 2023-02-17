import json
from operator import itemgetter
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from quiz_app.pagination import Mypagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from django.shortcuts import (
    get_object_or_404,
    get_list_or_404,
)
from django.db.models import (
    OuterRef,
    Count,
    Value,
    F,
)
from quiz_app.models import (
    Subject,
    Question,
)
from rest_framework.pagination import PageNumberPagination
# from authentication.authentication_api.serializer import (
#     SubjectListSerializer
# )
from quiz_app.quiz_api.serializer import (
    # SubjectSerializer,
    # QuestionSerializer,
    SubjectDetailSerializer,
    SubjectListSerializer,
    SubjectPostSerializer,
    QuestionPostSerializer,
    QuestionPagination,
    QuestionListSerializer
)


class SubjectListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_subject_list = get_list_or_404(Subject)
            serializer = SubjectListSerializer(get_subject_list,many=True)
            context = {
                    'status': status.HTTP_200_OK,
                    'success':True,
                    'response':serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)

        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_subject_name = self.request.query_params.get('subject_name')
            if get_subject_name:

                get_subject_list = Subject.objects.filter(subject_name__iexact=get_subject_name).annotate(
                    number_of_questions = Question.objects.filter(subject_id=OuterRef("id")
                                                ).values("subject_id"
                                                    ).annotate(number_of_questions=Count("id")).values("number_of_questions")
                    )

                serializer = SubjectDetailSerializer(get_subject_list,many=True,context = {"subject_name":get_subject_name})
                context = {
                    'status': status.HTTP_200_OK,
                    'success':True,
                    'response':serializer.data
                }
                return Response(context,status=status.HTTP_200_OK)
            else:
                context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':"Subject name must pass"
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


# class QuestionListView(APIView):
    
#     def get(self, request,*args, **kwargs):
#         try:
#             get_subject_name = self.request.query_params.get('subject_name')

#             get_question_qs = Question.objects.filter(
                                                    
#                                                     subject__subject_name__iexact=get_subject_name
#                                                                             ).select_related(
#                                                                                 'subject'
#                                                                                 )
#             serializer = QuestionSerializer(get_question_qs,many=True,context = {"subject_name":get_subject_name})
#             context = {
#                 'status':status.HTTP_200_OK,
#                 'success':True,
#                 'response':serializer.data,
#             }
#             return Response(context,status=status.HTTP_200_OK)

#         except Exception as exception:
#             context = {
#                 'status':status.HTTP_400_BAD_REQUEST,
#                 'success':False,
#                 'response':str(exception),
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)

class SubjectPostAPI(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]

    def post(self,request):
        try:
            data = request.data
            serializer = SubjectPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'status':status.HTTP_200_OK,
                    'success':True,
                    'response':serializer.data,
                }
                return Response(context,status=status.HTTP_200_OK)

            else:
                context = {
                    'status':status.HTTP_400_BAD_REQUEST,
                    'success':False,
                    'response':serializer.errors,
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class QuestionPostAPI(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes= [BasicAuthentication]
    def post(self, request):
        try:
            data = request.data
            serializer = QuestionPostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'status':status.HTTP_200_OK,
                    'success':True,
                    'response':serializer.data
                }
                return Response(context,status=status.HTTP_200_OK)
            else:
                context = {
                        'status':status.HTTP_400_BAD_REQUEST,
                        'success':False,
                        'response':serializer.errors,
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class QuestioinList(ListAPIView):
    serializer_class = QuestionListSerializer
    pagination_class = Mypagination

    def get_queryset(self):
        try:
            get_subject_name= self.request.query_params.get('subject_name')
            get_subject_question_obj = Question.objects.filter(
                                                subject__subject_name__iexact=get_subject_name
                                                                    ).select_related(
                                                                        'subject'
                                                                        ).order_by("-id")
            return get_subject_question_obj
        
        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class CorrectAnswerView(APIView):
    def post(self, request,*args, **kwargs):
        try:
            # get_selected_option = self.request.query_params.get('selected_option')
            get_json = request.POST.get('get_json',None)
            # print(get_json)
            get_json_obj = json.loads(get_json)
            print(get_json_obj,19)
            # length_of_json = len(get_json_obj)
            # print(length_of_json,20)
            count = 0
            # f = lambda 

            # for i in get_json_obj:
                # print(i,17)
            question_obj = Question.objects.all().values("id","answer")
            # lenght_of_question_obj = len(question_obj)
            # print(lenght_of_question_obj,1234)
            print(question_obj,18)
            # get_list = list(filter(lambda x:b))
            

            f = list( filter(lambda tag: tag['id'] == question_obj[0]['id'] and tag['op']==question_obj[0]['answer'], get_json_obj))
            print(f,17)

            # print(question_obj)
            # print(question_obj,17)
            if f:
                count += 1
            context = {
                'status': status.HTTP_200_OK,
                'success':True,
                'response':{"your_score":count}
            }
            return Response(context,status=status.HTTP_200_OK)

        except Exception as exception:
            context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        




