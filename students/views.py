from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from  students.models import Student

def f1(request):
    data=Student.objects.all()
    return render(request,"students/index.html",{"data":data})
