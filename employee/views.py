from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.views.generic import  View
from django.contrib import messages

# Create your views here.


class AddEmployee(View):
    def get(self,request):
        form=EmployeeForm()
        context={"form":form}
        return render(request,"add_employee.html",context)
    def post(self,request):
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"employee hasbeen addded")
            return redirect("addemp")
        else:
            messages.error(request,"employee adding failed")

            context={"form":form}
            return render(request, "add_employee.html", context)

class ListEmployees(View):
    def get(self,request):
        qs=Employee.objects.all()
        context={"employees":qs}
        return render(request,"list_emp.html",context)

