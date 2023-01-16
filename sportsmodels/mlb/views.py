from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "mlb/index.html")