from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from poll.models import Poll

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "poll/votar.html", {
            "polls": Poll.objects.all()
        })

def votar_view(request):
    if request.user.is_authenticated:
        return render(request, "poll/votar.html", {
            "polls": Poll.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("login"))
