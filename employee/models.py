from django.db import models

# Create your models here.
#
class Department(models.Model):
    dept_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    name=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.PositiveIntegerField()
    email=models.CharField(max_length=120,unique=True)
    phone=models.CharField(max_length=12)
    date_of_join=models.DateField(null=True)
    pic=models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


