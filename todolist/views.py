from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Read your Items here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {"items": items}
    # adding context as an argument in the render below insures we have access
    # to our items in the todo_list.html
    return render(request, "todo/todo_list.html", context)


# Add an Item
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

# Add an Item
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


# Update an Item
def edit_item(request, item_id):
    # Adding the item_id parameter as this is what we linked in the button
    # We need to get a copy of the specific item using the below method
    item = get_object_or_404(Item, id=item_id)
    # We need to create a Post handler to allow update of item
    if request.method == "POST":
        # Only change from the above is we pass the instance of the form
        # we are editing i.e. item_id
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("get_todo_list")
    # Now we will create an instance of the form using the below
    form = ItemForm(instance=item)
    context = {"form": form}
    return render(request, "todo/edit_item.html", context)


# Toggle "Done" on an Item
def toggle_item(request, item_id):
    # Adding the item_id parameter as this is what we linked in the button
    # We need to get a copy of the specific item using the below method
    item = get_object_or_404(Item, id=item_id)
    # Change the 'done' to the opposite using not
    item.done = not item.done
    item.save()
    return redirect("get_todo_list")


# Delete Item
def delete_item(request, item_id):
    # Adding the item_id parameter as this is what we linked in the button
    # We need to get a copy of the specific item using the below method
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
