from django.shortcuts import render
from crud.models import crudstudent
from django.contrib import messages
from crud.forms import stform

def stdisplay(request):
    result=crudstudent.objects.all()
    return render(request,"index.html",{"crudstudent":result})

def stinsert(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('address') and request.POST.get('mobile') and request.POST.get('gender'):
            savest=crudstudent()
            savest.name=request.POST.get('name')
            savest.email=request.POST.get('email')
            savest.address=request.POST.get('address')
            savest.mobile=request.POST.get('mobile')
            savest.gender=request.POST.get('gender')
            savest.save()
            messages.success(request,"The Record "+savest.name+" is saved successfully !")
            return render(request,"create.html")

    return render(request,"create.html")

def stedit(request,id):
    getstudentdetails= crudstudent.objects.get(id=id)
    return render(request,'edit.html',{"crudstudent":getstudentdetails})

def stupdate(request,id):
    stupdate=crudstudent.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The Student Record Updated Successfull")
        return render(request,"edit.html",{"crudstudent":stupdate})

def stdelete(request,id):
    deletestudent= crudstudent.objects.get(id=id)
    deletestudent.delete()
    result=crudstudent.objects.all()
    return render(request,"index.html",{"crudstudent":result})
