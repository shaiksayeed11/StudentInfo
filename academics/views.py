from django.shortcuts import render

# Create your views here.
from academics.models import Studentacademics
def f1(request):
    data=Studentacademics.objects.all()
    return render(request,"academics/index1.html",{"data":data})
