<<<<<<< HEAD
from django.db import models


from django.db import models
import datetime

=======
import datetime
>>>>>>> 3240e2301eb005813694940b3f5c5b72e1674087
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

<<<<<<< HEAD

=======
>>>>>>> 3240e2301eb005813694940b3f5c5b72e1674087
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
<<<<<<< HEAD
    
=======
>>>>>>> 3240e2301eb005813694940b3f5c5b72e1674087
    def __str__(self):
        return self.choice_text