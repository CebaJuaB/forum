from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Option(models.Model):
    answer = models.CharField(max_length=127)
    coeficient = models.DecimalField(max_digits=5, decimal_places=5, default=0)
    votes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.answer} coeficiente {self.coeficient} votes {self.votes} shares {self.shares}"

class Poll(models.Model):
    class Method(models.TextChoices):
        MAYORIA_CALIFICADA = 'MC', _('Mayoría Calificada')
        MAYORIA_SIMPLE = 'MS', _('Mayoría Simple')
        VERIFICA_QUORUM = 'QU', _('Verificación del cuórum')
    class Criteria(models.TextChoices):
        INDIVIDUAL = 'IN', _('Individual')
        COEFICIENT = 'CO', _('Coeficiente')
        SHARES = 'SH', _('Acciones')
    question = models.CharField(max_length=127)
    winning_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="winning")
    method = models.CharField(max_length=2, choices=Method.choices, default=Method.MAYORIA_CALIFICADA)
    parameter = models.DecimalField(max_digits=5, decimal_places=2,default=0.7)
    criteria = models.CharField(max_length=2, choices=Criteria.choices, default=Criteria.COEFICIENT)
    voters = models.IntegerField(default=0)
    total_shares = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.question} {self.criteria} contados {self.method} parámetro {self.parameter}" 

class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="choices")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    vote_time = models.DateTimeField()

    def __str__(self):
        return f"{self.option} hora {self.vote_time}" 