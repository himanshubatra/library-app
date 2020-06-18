from django import forms

from crudApp.models import Emp

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"