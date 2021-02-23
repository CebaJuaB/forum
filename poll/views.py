from django.shortcuts import render

from .models import Option

# Create your views here.
def index(request):
    return render(request, "poll/index.html", {
        "options": Option.objects.all()
    })
