from django.shortcuts import render

from .models import Option

# Create your views here.
def index(request):
    return render(request, "poll/index.html", {
        "options": Option.objects.all()
    })

def option(request, option_id):
    option = Option.objects.get(pk=option_id)
    return render(request, "poll/option.html", {
        "option": option
    })
