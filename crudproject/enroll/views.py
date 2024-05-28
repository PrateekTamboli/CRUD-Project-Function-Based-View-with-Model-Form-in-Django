from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# this function will add new item and show all items
def add_show(request):                  #this function use to render html files
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            ph = fm.cleaned_data['phone']
            reg = User(name=nm, email=em, password=pw, phone=ph) #data db me save hota h
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# this function will Edit    
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})
# this funtion will delete
def delete_data(request, id):
    if request.method == "POST":
            pi = User.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')
