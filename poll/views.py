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
        labels = []
        data_coeficient = []
        data_shares = []
        data_votes = []
        options = Option.objects.filter(poll=poll_id)
        for option in options :
            labels.append(option.answer)
            data_coeficient.append(float(option.coeficient))
            data_shares.append(option.shares)
            data_votes.append(option.votes)
        no_voters = User.objects.all()
        voted = []
        for vot in no_voters:
            if Vote.objects.filter(poll=poll_id,voter=vot).exists():
                voted.append(vot.id)
        return render(request, "poll/poll.html", {
            "poll": Poll.objects.get(pk=poll_id),
            "options": options,
            "votes": Vote.objects.filter(poll=poll_id).order_by('option'),
            "no_voters": no_voters.exclude(id__in=voted).order_by('first_name'),
            'labels': labels[:8],
            'data_coeficient': data_coeficient[:8],
            'data_shares': data_shares[:8],
            'data_votes': data_votes[:8],
            'colors': [ 'red', 'blue','yellow','green','orange','purple','white',"black"]
        })
    else:
        return HttpResponseRedirect(reverse("login"))