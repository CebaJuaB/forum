from django.shortcuts import render

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "vota/vota.html")

def vota_view(request):
    return render(request, "vota/vota.html")