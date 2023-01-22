import datetime
from django.shortcuts import render
from .models import PgaPreds

def index(request):
    allpreds = PgaPreds.objects.all()
    sorted_preds = sorted(allpreds, key=lambda x:x.position, reverse=False)
    context = {'allpreds':allpreds,
               'sorted_preds':sorted_preds}
    return render(request, "pga/index.html", context)