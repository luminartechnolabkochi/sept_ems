from django.forms import ModelForm
from .models import Employee
from  django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
           "name": forms.TextInput(attrs={"class":"form-control"}),
            "department": forms.Select(attrs={"class": "form-select"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_join": forms.DateInput(attrs={"class": "form-control","type":"date"})


        }