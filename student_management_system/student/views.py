from typing import DefaultDict
from django import forms
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import imageform,imageform1
from .models import student

# Create your views here.

class session1:
    def __init__(self,request,reg):
        self.reg=reg
        request.session['reg']=self.reg
        request.session.set_expiry(0)
        global versha
        versha = request.session.get('reg')



def login(request):
    if request.method=="POST":
        reg = request.POST['reg']
        if len(reg)==0:
            return  redirect('/login/')
        obj = student.objects.all().filter(reg_no=reg)
        if len(obj)>0:
            qw = session1(request,reg)
            return redirect("/home/")
        else:
            return redirect('/register/')
    if request.session.get('reg'):      
        return redirect('/home/')
    else:
        return render(request,'login.html')    

def logout(request):
    request.session.flush()
    request.session.clear_expired()
    return redirect ('/') 


        

   

def fetch_record(request):
    if  request.session.get('reg'):
        return render(request,"option.html")
    else:
        return redirect('/')

def register(request):
    if request.method=="POST":
        form=imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        form=imageform()
    return render(request,'register.html',{'form':form})

def sall(request):
    if request.session.get('reg'):      
        img=student.objects.all()
        return render(request,'show.html',{'img':img})
    else:
        return redirect('/')

def fetch(request):

    if request.method=="POST":
        if request.POST['name'] :
            print(request.POST['name'])
            global nam 
            nam=request.POST['name']
            img=student.objects.all().filter(reg_no=nam)
            print(type(img))
            if len(img)>0:
                return render(request,'show.html',{'img':img})
            else:
                return render(request,"fetch.html",{'err':'RECORD DOES NOT EXIST'})

    if request.session.get('reg'):      
        return render(request,"fetch.html",{'name':"SHOW"})
    else:
        return redirect('/')

def delete(request):
    if request.method=="POST":
        if request.POST['name']:
            nam=request.POST['name']
            name=request.session['reg']
            if nam==str(name):
                student.objects.all().filter(reg_no=nam).delete()
                return redirect('/')
            else:
                return render(request,'fetch.html',{'err':"YOU CAN'T DELETE OTHERS RECORD"})
    if request.session.get('reg'):
        return render(request,"fetch.html",{'name':"DELETE"})
    else:
        return redirect('/')


def update(request):
    global versha
    if request.method=="POST":
        name=request.POST['name']
        branch = request.POST['branch']
        student.objects.filter(reg_no=versha).update(name=name,branch=branch)
        return redirect('/')
    if  request.session.get('reg'):   
        sd = student.objects.filter(reg_no=versha)
        return render(request,'update.html',{'details':sd})
    else:
        return redirect('/')


def update_image(request):
    global versha
    if request.method=="POST":
        data=student.objects.get(reg_no=versha)
        form = imageform1(request.POST,request.FILES,instance=data)
        form.save()
        return redirect('/home/')
    else:
        if request.session.get('reg'):   
            sd=imageform1()
            return render(request,'new.html',{'details':sd})
        else:
            return redirect('/')


def im(request):
    return render(request,'image.html')




