from django.shortcuts import render

from homepage.models import Input
from homepage.forms import AddTextForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = AddTextForm(request.POST)
        form.save()
    
    form = AddTextForm()
    return render(request, "index.html", {"form": form})