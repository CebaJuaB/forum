from django.db import models
from datetime import date

# Create your models here.
class Option(models.Model):
    answer = models.CharField(max_length=127)
    coeficient = models.DecimalField(max_digits=5,decimal_places=5)
    votes = models.IntegerField()
    
    def __str__(self):
        return f"{self.answer} coeficiente {self.coeficient} votes {self.votes}"

class Poll(models.Model):
    question = models.CharField(max_length=127)
    winning_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.question}"