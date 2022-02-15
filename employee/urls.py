from django.urls import path
from . import views

urlpatterns=[
    path("add",views.AddEmployee.as_view(),name="addemp"),
    path("all",views.ListEmployees.as_view(),name="allemp")
]