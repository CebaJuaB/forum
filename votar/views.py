from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from poll.models import Poll, Option, Vote
from datetime import datetime
from django.db import transaction

import pytz

set(pytz.all_timezones_set)

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
        if not queryset.exists():
            tz = pytz.timezone('America/Bogota')
            vote_time = datetime.now(tz=tz)
            if vote_time > poll.start_time and vote_time < poll.end_time :
                return render(request, "poll/vota.html", {
                    "poll": poll,
                    "options": Option.objects.filter(poll=poll_id)
                })
            else :
                return render(request, "poll/votar.html", {
                "message": "Está fuera del horario de la votación seleccionada.",
                "polls": Poll.objects.all()
                })
        else :
            return render(request, "poll/votar.html", {
                "message": "Ya participó en la votación seleccionada.",
                "polls": Poll.objects.all()
                })
    else:
        return HttpResponseRedirect(reverse("login"))

def votacion_view(request, poll_id):
    if request.method == "POST":
        tz = pytz.timezone('America/Bogota')
        vote_time = datetime.now(tz=tz)
        poll = Poll.objects.get(pk=poll_id)
        voter = request.user
        with transaction.atomic():
            option = Option.objects.select_for_update().filter(pk=int(request.POST["option"])).first()
            option.coeficient += voter.profile.coeficient 
            option.shares += voter.profile.shares 
            option.votes += 1
            option.save()
        voto = Vote(poll=poll, option=option, voter=voter, vote_time=vote_time)
        voto.save()
        return HttpResponseRedirect(reverse("poll", args=(poll.id,)))