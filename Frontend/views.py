from django.shortcuts import render,redirect
from backend.models import addmoviedb,addrate
from Frontend.models import customerDb
def homepage(q):
    data=addmoviedb.objects.all()
    da = addrate.objects.all()
    return render(q,"Home.html",{'data':data, 'da':da})

def loginP(q):
    return render(q,"LOGIN.html")
def registerSave(q):
    if q.method =="POST":
        a=q.POST.get('username')
        b=q.POST.get('email')
        c=q.POST.get('password')
        d=q.POST.get('confirm')
        obj=customerDb(Username=a,Email=b,Password=c,Confirmpassword=d)
        obj.save()
        return redirect(homepage)
def loginPAGE(q):
    return render(q,"newlogin.html")
def custlogin(q):
    if q.method=="POST":
        username_r=q.POST.get("username")
        password_r=q.POST.get("password")
        if customerDb.objects.filter(Username=username_r,Password=password_r).exists():
            q.session['username']=username_r
            q.session['password']=password_r

            return redirect(booking)

        else:
            return redirect(loginPAGE)
def userlogout(q):
    del q.session['username']
    del q.session['password']
    return redirect(homepage)
def booking(q):
    return render(q,"Booking.html")

def returntopage(q):
    return redirect(homepage)

def contactpage(q):
    return render(q,"contact.html")
def contactsave(q):
    return redirect(homepage)