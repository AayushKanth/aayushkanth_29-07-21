from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ToDoForm
from .models import ToDoList

def index(request):
    item_list = ToDoList.objects.order_by("-date")
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ToDoList')
    form = ToDoForm()

    page = {
        "forms" : form,
        "list" : item_list,
        "title" : "TODO LIST",
    }
    return render(request, 'index.html', page)

def remove(request, item_id):
    item = ToDoList.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item has been Removed !")
    return redirect('ToDoList')

# Create your views here.
