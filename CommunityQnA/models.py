from django.db import models

# Create your models here.
class QnA(models.Model):
    question_no = models.IntegerField(unique=True)
    question = models.CharField(max_length=5000, default='Ask Anything')
    posted_on = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField('answer_status', default=False)
    answer = models.CharField(max_length=5000, blank = True) 
    
    class Meta:
        verbose_name = "QnA"
        verbose_name_plural = "QnAs"


