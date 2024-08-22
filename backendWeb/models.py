import datetime

from django.db import models
from django.utils import timezone
# Qeustion erbt von models.Model
class Question(models.Model):  # Model erstellen, um auf SQLite-datenbank zuzugreifen
    question_head = models.CharField(max_length=100, default="empty")
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    
    
    def __str__(self):
        return self.question_head
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
       # return f'{self.question_text} Veröffentlicht: {self.pub_date}'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text