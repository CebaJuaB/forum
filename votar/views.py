from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from datetime import datetime

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
        poll = Poll.objects.get(pk=poll_id)
        voter = request.user
        queryset = Vote.objects.filter(poll=poll, voter=voter)
        return render(request, "poll/vota.html", {
            "poll": poll,
            "options": Option.objects.filter(poll=poll_id)
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def votacion_view(request, poll_id):
    if request.method == "POST":
        option = Option.objects.get(pk=int(request.POST["option"]))
        poll = Poll.objects.get(pk=poll_id)
        voter = request.user
        vote_time = datetime.now()

        option.coeficient = voter.profile.coeficient + option.coeficient
        option.shares = voter.profile.shares + option.shares
        option.votes = option.votes + 1
        option.save()

        voto = Vote(poll=poll, option=option, voter=voter, vote_time=vote_time)
        voto.save()
        
        return HttpResponseRedirect(reverse("poll", args=(poll.id,)))