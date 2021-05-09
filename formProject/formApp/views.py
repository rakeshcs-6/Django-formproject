from django.shortcuts import render
from formApp.forms import student
# Create your views here.
def view(request):
    f=student()
    if request.method=="POST":
        f=student(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            marks=f.cleaned_data['marks']
            d={"name1":name,"roll1":roll,"marks1":marks}
            return render(request,"formApp/output.html",d)
    d={"form":f}
    return render(request,"formApp/input.html",d)