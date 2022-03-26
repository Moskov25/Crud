from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#this function show and add items
def add_show(request):
    if request.method  == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        #for clearing fields after entring and submiting data
        fm = StudentRegistration()
    stud= User.objects.all()
    return render(request,'enroll/addshow.html', {'form':fm,'stu':stud}) 

    return render(request, 'enroll/addshow.html' ,{'form':fm})
#this function will update or delete 
def update_data(request, id):
 if request.method == 'POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST, instance=pi)
     if fm.is_valid():
      fm.save()  
 else:
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request,'enroll/updatestudent.html',{'form':fm})
  

    #this function delete data (After describing this define its URL on Project/url.py)
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        #pk=primary key
        pi.delete() 
        return HttpResponseRedirect('/')