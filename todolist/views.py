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


# def add_item(request):
#     if request.method == "POST":
#         # here we will create variables that will take the attributes
#         # required by the Item model which in this case is 'name' and
#         # 'done' and we canget these values from the name fields provided
#         #  in the form i.e. item_name & done
#         name = request.POST.get("item_name")
#         # getting the done status is slightly different because its a
#         # checkbox, to check if the item is done we need to check the POST
#         # data to see if it contains 'done' property
#         done = "done" in request.POST
#         # To create the Item we need to do the below and provided the 2
#         # variables to match the atttributes required i.e. 'name' & 'done'
#         Item.objects.create(name=name, done=done)
#         # We then want to redirect the user back to the todo list
#         return redirect("get_todo_list")
#     # Now we can create an instance of the ItemForm
#     form = ItemForm()
#     context = {"form": form}
#     # adding context as an argument in the render below insures we have
#     # access to our form in the add_item.html
#     return render(request, "todo/add_item.html", context)


def add_item(request):
    if request.method == "POST":
        # Instead of trying to create the form manually lets let the new form
        # from forms.py do it, to do that we can use the similar syntax to
        # create the empty form but instead we will use the POST data
        form = ItemForm(request.POST)
        # We can then call the is_valid method which will check that the form
        # matches the fields required by the model i.e. 'name' & 'done'
        if form.is_valid():
            # to save our form we just need to run:
            form.save()
        return redirect("get_todo_list")
    # Now we can create an instance of the ItemForm
    form = ItemForm()
    context = {"form": form}
    # adding context as an argument in the render below insures we have access
    # to our form in the add_item.html
    return render(request, "todo/add_item.html", context)
