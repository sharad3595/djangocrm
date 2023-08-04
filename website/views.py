from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record



def sign_up_page(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'register.html',{'form':form})

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!!")
            return redirect('dashboard')
        else:
            messages.success(request, "Login failed! Please try again!!")
            return redirect('home')        
    else:
        return render(request, "dashboard.html")


def record(request):
    records = Record.objects.all()
    return render(request, 'records.html',{'records':records})


def single_record(request,pk):
    if request.user.is_authenticated:
        single_record = Record.objects.get(id=pk)
        return render(request, 'single_record.html',{'single_record':single_record})
    else:
        messages.success(request,'You must login to view customer record!!')
        return render(request,'user_login.html')
    

def single_record_delete(request,pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request,"Record Deleted Successfully!")
        return redirect('record')
    else:
        messages.success(request,'You must login to perfor this operation!')
        return render(request,'user_login.html')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"New Record Added Successfully!!")
                return redirect('record')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You need to login to perform this operation!!")
        return render(request,'user_login.html',)
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated Successfully!")
            return redirect('record')
        return render(request,'update_record.html',{'form':form})    
    else:
        messages.success(request,"You must login to perform this operation!")
        return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout successfully!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           #Authenticate user
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request,user)
           messages.success(request, "User created successfully! Welcome")
           return redirect('home') 
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    
    return render(request, 'register.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')
    # if request.user.is_authenticated:
    #     return render(request,'dashboard_base.html')
    # else:
    #     return redirect('home')
