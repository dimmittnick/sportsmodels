from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "nhl/index.html")

def nick(request):
    return HttpResponse("hello, Nick")

def greet(request, name):
    return render(request, "nhl/greet.html", {
        "name":name.capitalize()
    })