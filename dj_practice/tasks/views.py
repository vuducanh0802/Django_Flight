from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Grade",min_value=1,max_value=5)


tasks = [] 
task = ["foo","bar","baz"]

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    return render(request,"tasks/index.html",{
        # "tasks":tasks
        "tasks": request.session['tasks']
    })


def add(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # tasks.append(task)
            request.session['tasks'] += [task]
            return HttpResponseRedirect("/tasks")
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })

    return render(request, 'tasks/add.html',{
        "form":NewTaskForm()
    }) 