from django.shortcuts import render
from . import forms
# Create your views here.

def home(request):
    return render(request,'main/index.html')

def register(request):
    msg=None
    form = forms.RegisterUser
    if request.method=='POST':
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Registered'
    return render(request,'registration/register.html',{'form':form,'msg':msg})
