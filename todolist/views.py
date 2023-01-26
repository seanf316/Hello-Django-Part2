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
    # if request.method == "POST":
    #     # get attributes from the form name i.e. item_name & done
    #     name = request.POST.get("item_name")
    #     # checkboxs slightly different we need to check if the POST status
    #     # has 'done' in it
    #     done = "done" in request.POST
    #     # To create the item we need to provide the 2 attributes of the item
    #     # model which in this case is name & done, we have set the variables
    #     # above and called them name & done so create a new item
    #     # we do the below
    #     Item.objects.create(name=name, done=done)
    #     # we then want to redirect the user back to the Todo page
    #     return redirect("get_todo_list")
    #     # With the form added we can create an instance of the form below:
    #     form = ItemForm()
    #     # create a context which contains an empty form
    #     context = {"form": form}
    #     # adding context as an argument in the render below insures we have
    #     # access to our form in the add_item.html
    return render(request, "todo/add_item.html")
