from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.contrib.auth.models import User

from poll.models import Poll, Option, Vote

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "poll/votar.html", {
            "polls": Poll.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def voto_view(request, poll_id):
    if request.user.is_authenticated:
        return render(request, "poll/vota.html", {
            "poll": Poll.objects.get(pk=poll_id),
            "options": Option.objects.filter(poll=poll_id)
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def votacion_view(request, poll_id):
    if request.method == "POST":
        option = Option.objects.get(pk=int(request.POST["option"]))
        poll = Poll.objects.get(pk=poll_id)
        voto = Vote(poll=poll, option=option, voter=request.user)
        voto.save()
        return HttpResponseRedirect(reverse("votar", args=(poll.id,)))