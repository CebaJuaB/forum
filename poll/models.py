from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    class Method(models.TextChoices):
        MAYORIA_CALIFICADA = 'Mayoria Calificada'
        MAYORIA_SIMPLE = 'Mayoría Simple'
        VERIFICA_QUORUM = 'Verificación del Quorum'
    class Criteria(models.TextChoices):
        INDIVIDUAL = 'Individual'
        COEFICIENT = 'Coeficiente'
        SHARES = 'Acciones'
    question = models.CharField(max_length=127)
    method = models.CharField(max_length=23, choices=Method.choices, default=Method.MAYORIA_CALIFICADA)
    parameter = models.DecimalField(max_digits=5, decimal_places=2,default=0.7)
    criteria = models.CharField(max_length=11, choices=Criteria.choices, default=Criteria.COEFICIENT)
    max_voters = models.IntegerField(default=0)
    max_shares = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return f"{self.question}" 

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll")
    answer = models.CharField(max_length=127)
    coeficient = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)
    votes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.answer}"

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="questions")
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="choices")
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    vote_time = models.DateTimeField()
    def __str__(self):
        return f"Pregunta: {self.poll} Opción: {self.option}. Fecha y hora: {self.vote_time} - Votante: {self.voter} " 