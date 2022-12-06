from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

class Topic(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    t_name = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.t_name


class Question(models.Model):
    t_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    quetion = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.quetion

class Option(models.Model):
    option = models.CharField(max_length=255)
    is_right = models.BooleanField()
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.option

class User(models.Model):
    ferst_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=12)
    admin = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.ferst_name
    
class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    quiz_title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.quiz_title

class Result_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=255)
    is_solved = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.question_name