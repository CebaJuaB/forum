from django.shortcuts import render

from .models import Option, Poll
# Create your views here.
def index(request):
    return render(request, "poll/index.html", {
        "polls": Poll.objects.all()
    })

def option_view(request, poll_id, option_id):
    return render(request, "poll/option.html", {
        "poll": Poll.objects.get(pk=poll_id),
        "option": Option.objects.get(pk=option_id, poll=poll_id)
    })

def poll_view(request, poll_id):
    return render(request, "poll/poll.html", {
        "poll": Poll.objects.get(pk=poll_id),
        "options": Option.objects.filter(poll=poll_id)
    })