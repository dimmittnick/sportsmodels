from django.http import HttpResponse
from django.shortcuts import render
from .models import NhlPreds
from datetime import *

today = datetime.today().strftime("%Y-%m-%d")

def index(request):
    allpreds = NhlPreds.objects.filter(date=today)
    sorted_preds = sorted(allpreds, key=lambda x:x.prediction, reverse=True)
    context = {'allpreds':allpreds,
               'sorted_preds':sorted_preds}
    return render(request, "nhl/index.html", context)

