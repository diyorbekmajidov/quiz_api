from rest_framework import serializers
from api.models import (
    Quiz,
    Topic,
    Question,
    Option,
    User,
    Result,
    Result_detail
)

class Quiz_serilaizers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class Topic_serilaizers(serializers.ModelSerializer):
    class Meta:
        quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
        model = Topic
        fields = '__all__'

class Question_serilaizers(serializers.ModelSerializer):
    class Meta:
        t_name = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
        model = Question
        fields = '__all__'

class Option_serilaizers(serializers.ModelSerializer):
    class Meta:
        quetion = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        model = Option
        fields = '__all__'
        
class User_serilaizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Result_serializers(serializers.ModelSerializer):
    class Meta:
        user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        model = Result
        fields = '__all__'

class Result_detailserilaizers(serializers.ModelSerializer):
    class Meta:
        user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all)
        result_id = serializers.PrimaryKeyRelatedField(queryset=Result.objects.all())
        model = Result_detail
        fields = '__all__'