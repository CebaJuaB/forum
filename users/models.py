from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shares = models.IntegerField(default=0)
    coeficient = models.DecimalField(max_digits=4, decimal_places=4, default=0)
    document = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} acciones {self.shares} coeficiente {self.coeficient} document {self.document}" 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()