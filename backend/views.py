from django.shortcuts import render,redirect
from backend.models import addrate,addmoviedb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

def indexpage(q):
    return render(q,"index.html")
def arating(q):
    return render(q,"addrating.html")
def saverating(q):
    if q.method == "POST":
        a=q.POST.get('category')
        b=q.POST.get('rating')
        obj=addrate(Category=a,Rating=b)
        obj.save()
        return redirect(arating)
def addm(q):
    return render(q,"addmovies.html")
def addmoviesave(q):
    if q.method=="POST":
        a=q.POST.get('language')
        b=q.POST.get('category')
        c=q.POST.get('name')
        f=q.FILES['image']
        obj=addmoviedb(Language=a,Category=b,Name=c,Image=f)
        obj.save()
        return redirect(addm)
def displayrating(q):
    data=addrate.objects.all
    return render(q,"displayrating.html",{'data':data})
def displaymovie(q):
    data=addmoviedb.objects.all
    return render(q,"displaymovies.html", {'data':data})
def editrating(q,dataid):
    data=addrate.objects.get(id=dataid)
    return render(q,"editrate.html", {'data':data})
def updaterating(q,dataid):
    if q.method=="POST":
        a=q.POST.get('category')
        b=q.POST.get('rating')
        addrate.objects.filter(id=dataid).update(Category=a,Rating=b)
        return redirect(displayrating)
def deleterate(q,dataid):
    data=addrate.objects.filter(id=dataid)
    data.delete()
    return redirect(displayrating)
def editmovie(q,dataid):
    data=addmoviedb.objects.get(id=dataid)
    return render(q,"editmovies.html", {'data':data})
def updatemovie(q,dataid):
    if q.method=="POST":
        a=q.POST.get('language')
        b=q.POST.get('category')
        c=q.POST.get('name')
        try:
            img=q.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=addmoviedb.objects.get(id=dataid).Image
        addmoviedb.objects.filter(id=dataid).update(Language=a,Category=b,Name=c,Image=file)
        return redirect(displaymovie)

def deletemovie(q,dataid):
    data=addmoviedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymovie)

def loginpag(q):
    return render(q,"loginpage.html")
def adminlogin(q):
    if q.method=="POST":
        username_r=q.POST.get('username')
        password_r=q.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)

            if user is not None:
                login(q,user)
                q.session['username']=username_r
                q.session['password']=password_r
                messages.success(q,"Login successfull")
                return redirect(indexpage)
            else:
                messages.error(q,"invalid user")
                return redirect(loginpag)
        else:
            messages.error(q,"invalid user")
            return redirect(loginpag)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpag)