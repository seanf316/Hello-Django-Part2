from django import forms
from .models import Item

# Created forms using django allows django to look after the
# validation/requirements
# Created a form and missing a field that is required in the
# database can cause errors with Django


# forms are inherited from django.forms using form.ModelForm
class ItemForm(forms.ModelForm):
    # To tell the form which model it is associated with we will include
    # and inner Class called 'Meta', this provides the form with some
    # information about itself like - fields it should render, how it
    # should display error messages and so on.
    class Meta:
        model = Item
        # fields below are what we want the form to display
        fields = ["name", "done"]

    # The idea of creating or own form in django is that rather then creating
    # a form in html we can render it out as a variable, to make sure its
    # availale in the template updated the views.py file with the below
    # from .forms import ItemForm
