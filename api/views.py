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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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