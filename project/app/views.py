from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def superadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        details = User.objects.create(username=username, email=email)
        return redirect('home')
    return render(request,'superadmin.html')   


def home(request):
    details = User.objects.all()
    return render(request,'home.html',{'details':details})


def delete(request,id):
    query = User.objects.get(pk=id)
    query.delete()
    return redirect('home')

def edit(request,id):
    details = User.objects.get(pk=id)

    if request.method == 'POST':
        details.username = request.POST['username']
        details.email = request.POST['email']
        
        details.save()

        return redirect('home')
    
    return render(request,'edit.html',{'details': details})


# Create your views here.
