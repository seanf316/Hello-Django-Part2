from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {"items": items}
    # adding context as an argument in the render below insures we have access
    # to our items in the todo_list.html
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    return render(request, "todo/add_item.html")
