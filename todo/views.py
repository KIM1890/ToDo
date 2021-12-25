from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django.http import Http404
# Create your views here.


def home(request):
    try:
        task_list = Task.objects.order_by('-date')
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todo')
        form = TaskForm()
        page = {
            'forms': form,
            'task_list': task_list,
            'title': 'TO-DO-LIST'
        }
    except Task.DoesNotExist:
        raise Http404('ToDo does not exist')
    return render(request, 'todo.html', page)


def update(request, task_id):

    item = Task.objects.get(id=task_id)

    # pass the object as instance in form
    form = TaskForm(instance=item)

    # save the data from the form and
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo')

    # add form dictionary to context
    page = {"forms": form}

    return render(request, "todo.html", page)


def remove(request, task_id):
    item = Task.objects.get(id=task_id)
    if request.method == "POST":
        item.delete()
        return redirect('todo')
    page = {'item': item}
    return render(request, 'delete.html', page)
