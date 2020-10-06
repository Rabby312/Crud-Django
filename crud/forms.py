from django import forms
from crud.models import crudstudent

class stform(forms.ModelForm):
    class Meta:
        model=crudstudent
        fields="__all__"
