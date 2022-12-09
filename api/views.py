from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
from .models import (
    Quiz, 
    Topic, 
    Question, 
    Option, 
    User, 
    Result, 
    Result_detail
)
from .serializers import (
    Quiz_serilaizers, 
    Topic_serilaizers,
    Question_serilaizers,
    Option_serilaizers,
    User_serilaizers,
    Result_serializers,
    Result_detailserilaizers
)

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Quiz_all(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request:Request):
        quiz = Quiz.objects.all()
        serializer = Quiz_serilaizers(quiz, many=True)
        return Response(serializer.data)

    def post(self, request:Request):
        data = request.data
        serializer = Quiz_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Topic_all(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request:Request, pk):
        quiz = Quiz.objects.get(id = pk)
        topic = Topic.objects.filter(quiz = quiz)
        serilaizer1 = Quiz_serilaizers(quiz, many = False)
        serilaizer = Topic_serilaizers(topic, many = True)
        data = {
            'quiz':serilaizer1.data,
            'topic':serilaizer.data
        }
        return Response(data)

    def post(self, request:Request):
        data=request.data
        serializer=Topic_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Question_all(APIView):
    def get(self, request:Request, pk):
        topic_filter=Topic.objects.get(id=pk)
        topic = Topic_serilaizers(topic_filter, many = False)

        quetion_id = Question.objects.filter(t_name=topic.data['id'])
        quetion = Question_serilaizers(quetion_id, many = True)

        data=[]
        for i in quetion.data:
            options = Option.objects.filter(quetion=i['id'])
            option_serializer = Option_serilaizers(options, many=True) 
            data.append({
                'quetion':i['quetion'],
                'id':i["id"],
                'options':option_serializer.data    
            })
        return Response(data)

    def post(request:Request):
        """"
        create question 
        """
        data=data.request
        serializer=Quiz_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class Result_detail_all(APIView):
    def post(request:Request):
        pass