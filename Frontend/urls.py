from Frontend import views
from django.urls import path
urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('loginP/',views.loginP,name="loginP"),
    path('registerSave/',views.registerSave,name="registerSave"),
    path('loginPAGE/',views.loginPAGE,name="loginPAGE"),
    path('custlogin/',views.custlogin,name="custlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('booking/',views.booking,name="booking"),
    path('returntopage/',views.returntopage,name="returntopage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('contactsave/',views.contactsave,name="contactsave")
]