from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        # When the form is invalid it will provide a dictionary
        # of errors in the forms fields so we can be more specific
        # with our test
        self.assertIn("name", form.errors.keys())
        # To further drive home the test we will check if the error
        # mesaage states this field is required
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        form = ItemForm({"name": "Test Todo Item"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])
