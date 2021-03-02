from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Option, Poll

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
        return render(request, "poll/poll.html", {
            "poll": Poll.objects.get(pk=poll_id),
            "options": Option.objects.filter(poll=poll_id)
        })
    else:
        return HttpResponseRedirect(reverse("login"))