from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Question(models.Model):
    title = models.CharField('Question', max_length=255)
    ANSWER_TYPE = (
        (1, 'Single'),
        (2, 'Multiple')
    )
    type = models.SmallIntegerField('Type', choices=ANSWER_TYPE, default=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField('Answer', max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer


class FriendshipTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_tests')
    name = models.CharField('Name', max_length=100)
    answers = models.ManyToManyField(Answer, related_name="my_answers", blank=True)
    code = models.UUIDField('Unique Code', default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
