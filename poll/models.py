from django.db import models
from datetime import date

# Create your models here.
class Poll(models.Model):
    class Method(models.TextChoices):
        MAYORIA_CALIFICADA = 'MC'
        MAYORIA_SIMPLE = 'MS'
        VERIFICA_QUORUM = 'VQ'
    class Criteria(models.TextChoices):
        INDIVIDUAL = 'IN'
        COEFICIENT = 'CO'
        SHARES = 'SH'
    question = models.CharField(max_length=127)
    method = models.CharField(max_length=2, choices=Method.choices, default=Method.MAYORIA_CALIFICADA)
    parameter = models.DecimalField(max_digits=5, decimal_places=2,default=0.7)
    criteria = models.CharField(max_length=2, choices=Criteria.choices, default=Criteria.COEFICIENT)
    max_voters = models.IntegerField(default=0)
    max_shares = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return f"{self.question}" 

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll")
    answer = models.CharField(max_length=127)
    coeficient = models.DecimalField(max_digits=3, decimal_places=3, default=0.0)
    votes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.answer}"

class Voter(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.first} {self.last}" 

class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="choices")
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name="voters")
    vote_time = models.DateTimeField()
    def __str__(self):
        return f"Opción {self.option} hora {self.vote_time} votó {self.voter}" 
