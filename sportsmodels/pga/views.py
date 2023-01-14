import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "pga/index.html", {
        "birthday": now.month == 9 and now.day == 3
    })