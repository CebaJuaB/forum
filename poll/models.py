from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Option(models.Model):
    answer = models.CharField(max_length=127)
    coeficient = models.DecimalField(max_digits=8, decimal_places=5)
    votes = models.IntegerField()
    
    def __str__(self):
        return f"{self.answer} coeficiente {self.coeficient} votes {self.votes}"

class Poll(models.Model):
    class Method(models.TextChoices):
        MAYORIA_CALIFICADA = 'MC', _('Mayoría Calificada')
        MAYORIA_SIMPLE = 'MS', _('Mayoría Simple')
    question = models.CharField(max_length=127)
    winning_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="winning")
    method = models.CharField(max_length=2, choices=Method.choices, default=Method.MAYORIA_CALIFICADA)
    parameter = models.DecimalField(max_digits=5, decimal_places=2,default=0.7)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.question}"