from backend import views
from django.urls import path
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('arating/',views.arating,name="arating"),
    path('saverating/',views.saverating,name="saverating"),
    path('addm/',views.addm,name="addm"),
    path('addmoviesave/',views.addmoviesave,name="addmoviesave"),
    path('displayrating/',views.displayrating,name="displayrating"),
    path('displaymovie/',views.displaymovie,name="displaymovie"),
    path('loginpag/',views.loginpag,name="loginpag"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('editrating/<int:dataid>/',views.editrating,name="editrating"),
    path('updaterating/<int:dataid>/',views.updaterating,name="updaterating"),
    path('deleterate/<int:dataid>/',views.deleterate,name="deleterate"),
    path('editmovie/<int:dataid>/',views.editmovie,name="editmovie"),
    path('updatemovie/<int:dataid>/',views.updatemovie,name="updatemovie"),
    path('deletemovie/<int:dataid>/',views.deletemovie,name="deletemovie"),
    path('adminlogout/',views.adminlogout,name="adminlogout")

]