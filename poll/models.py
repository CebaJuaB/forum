from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=127)
    winning_option = models.CharField(max_length=127)
    winning_coeficient = models.DecimalField()
    horario_inicio = models.DateTimeField()
    horario_fin = models.DateTimeField()