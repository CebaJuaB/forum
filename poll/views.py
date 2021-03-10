from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Option, Poll, Vote
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "poll/index.html", {
            "polls": Poll.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def poll_view(request, poll_id):
    if request.user.is_authenticated:
        no_voters = User.objects.all()
        to_be_deleted = []
        for vot in no_voters:
            if Vote.objects.filter(poll=poll_id,voter=vot).exists():
                to_be_deleted.append(vot.id)
        return render(request, "poll/poll.html", {
            "poll": Poll.objects.get(pk=poll_id),
            "options": Option.objects.filter(poll=poll_id),
            "votes": Vote.objects.filter(poll=poll_id).order_by('option'),
            "no_voters": no_voters.exclude(id__in=to_be_deleted)
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def no_voters():
        to_be_deleted = []
        for vot in no_voters:
            if Vote.objects.filter(poll=poll_id,voter=vot).exists():
                to_be_deleted.append(vot.id)
        no_voters.exclude(id__in=to_be_deleted)