from django.http import HttpResponse
from django.shortcuts import render
from .models import NhlPreds

def index(request):
    return render(request, "nhl/index.html", {
        "preds": NhlPreds.objects.all()
    })

