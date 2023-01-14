from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    ## make individual list for each user by making sessions
    ## if user doesnt have list, make them an empty one
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "mlb/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    ## updating to do list with a post
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        ## append new value to tasks list
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            ## redirect user to to do list 
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "mlb/add.html", {
                "form":form
            })

    return render(request, "mlb/add.html", {
        "form": NewTaskForm()
    })