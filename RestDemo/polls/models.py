from django.db import models


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    class Meta:
        db_table = u'"restdemo\".\"question"'
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        db_table = u'"restdemo\".\"choice"'
    
    def __str__(self):
        return self.choice_text
# Create your models here.
