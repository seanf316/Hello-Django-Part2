from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # prevents items from not having a name programmatically
    # blank makes field required on forms
    done = models.BooleanField(null=False, blank=False, default=False)
    # default set to False makes sure todo items are not set to done by default

    # this will return the Items name attribute in the Django Admin dashboard
    def __str__(self):
        return self.name
