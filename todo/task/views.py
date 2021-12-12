from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django.http import Http404


# Create your views here.
def home(request):
    try:
        task_list = Task.objects.order_by("-date")
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task')
        form = TaskForm()
        page = {
            'forms': form,
            "task_list": task_list,
            'title': "TO-DO-LIST"
        }
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('task')
