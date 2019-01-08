"""SSN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from app.views import Facultiesdetails, getecelist, listcse, ecelist, eeelist, meclist, Dfacultycivil, DSincefa, \
    DElectronicsf, DElectricals, DMechanicalfd, deletecivilf, updatecivilf, deletecsefa, updatecseup, \
    deleteece, updatefece, deletefeee, updatefeee, deletefme, updatefme, civilstudents, csestudentlist, eceliststudents, \
    eeeliststudents, mecliststudents, deletecivil, updatescivil, reviews, deletemassege, updatemassegs, openreviews, \
    updateCSEstudent, deletecse, upadateece, Deleteece, updateseee, deleteeee, updatesme, deleteme, updateECEF, \
    deleteECEF, deleteEEE, updatecEEE, deleteME, updateME

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex),
    path('Back/',views.Back),
    path('Compus/',views.Compus),
    path('Contact/',views.Contact),
    path('boysgirl/',views.boysgirl),
    path('hostellibrary/',views.hostellibrary),
    path('Transport/',views.Transport),
    path('sports/',views.sports),
    path('Training/',views.Training),
    path('Abouttap/',views.Abouttap),
    path('Placements/',views.Placements),
    path('openHomePage/',views.openHomePage),
    path('openAbout/',views.openssnabout),
    path('Admissions/',views.Admissions),
    path('Freessn/',views.Ssnfrees),
    path('Shcolarship/',views.Shcolarship),
    path('Acadamics/',views.Acadamics),
    path('Program/',views.Program),
    path('shchedual/',views.shchedual),
    path('Examination/',views.Examination),
    path('Awards/',views.Awards),
    path('Civil/',views.Civil),
    path('Since/',views.Since),
    path('Electronics/',views.Electronics),
    path('Electrical/',views.Electrical),
    path('Mechanical/',views.Mechanical),
    path('Rules/',views.Rules),
    path('malparc/',views.malparc),
    path('Result/',views.Result),
    path('google/',views.google),
    path('Departments/',views.Departments),
    path('Dcivil/',views.Dcivil),
    path('DSince/',views.DSince),
    path('DElectrical/',views.DElectrical),
    path('DElectronics/',views.DElectronics),
    path('DMechanical/',views.DMechanical),
    path('Dprogramsc/',views.Dprogramsc),
    path('Dstudentc/',views.Dstudentc),
    path('Dgalleryc/',views.Dgalleryc),
    path('DSincep/',views.DSincep),
    path('DSincesa/',views.DSincesa),
    path('DSincepg/',views.DSincepg),
    path('DElectronicsp/',views.DElectronicsp),
    path('DElectronicssa/',views.DElectronicssa),
    path('DElectronicsga/',views.DElectronicsga),
    path('DElectricalpo/',views.DElectricalpo),
    path('DElectricalsd/',views.DElectricalsd),
    path('DElectricalga/',views.DElectricalga),
    path('DMechanicalpo/',views.DMechanicalpo),
    path('DMechanicalsd/',views.DMechanicalsd),
    path('DMechanicalga/',views.DMechanicalga),
    path('Admin/',views.Admin),
    path('adminlogin/',views.adminlogin),
    path('logout/',views.logout),
    path('studentregistation/',views.studentregistation),
    # path('savestudentdetails/',views.savestudentdetails),
    # path('studentdetails/',StudentDetailslist.as_view(),name='name'),
    path('studentdetails/',views.studentdetails),
    path('facultyregistation/',views.facultyregistation),
    path('civilregistation/',views.civilregistation),
    path('civildetails/',views.civildetails),
    path('cseregistation/',views.cseregistation),
    path('cseregistationdetails/',views.cseregistationdetails),
    path('eceregistation/',views.eceregistation),
    path('eceregistationdetails/',views.eceregistationdetails),
    path('eeeregistation/',views.eeeregistation),
    path('saveeee/',views.saveeee),
    path('mecregistation/',views.mecregistation),
    path('mecsavedeatails/',views.mecsavedeatails),
    path('listcivil/',Facultiesdetails.as_view(template_name="admin.html"),name='civilf'),
    path('facaltylist/',views.facaltylist),
    path('listcse/',listcse.as_view(template_name="admin.html"),name='csef'),
    path('ecelist/',ecelist.as_view(template_name="admin.html"),name='ecef'),
    path('eeelist/',eeelist.as_view(template_name="admin.html"),name='eeef'),
    path('meclist/',meclist.as_view(template_name="admin.html"),name='mef'),
    path('Dfacultycivil/',Dfacultycivil.as_view( context_object_name='fcivil') ),
    path('DSincefa/',DSincefa.as_view( context_object_name='fsince') ),
    path('DElectronicsf/',DElectronicsf.as_view( context_object_name='fece') ),
    path('DElectricals/',DElectricals.as_view( context_object_name='feee') ),
    path('DMechanicalfd/',DMechanicalfd.as_view( context_object_name='fme') ),
    path('DMechanicalfd/',DMechanicalfd.as_view( context_object_name='fme') ),
    # path('deletes/<str:pk>/',deletes.as_view()),
    # path('updates/<str:pk>/',updates.as_view()),
    path('deletecivilf/<str:pk>/',deletecivilf.as_view()),
    path('deleteME/<str:pk>/',deleteME.as_view()),
    path('updateME/<str:pk>/',updateME.as_view()),
    path('deleteEEE/<str:pk>/',deleteEEE.as_view()),
    path('updatecEEE/<str:pk>/',updatecEEE.as_view()),
    path('updateECEF/<str:pk>/',updateECEF.as_view()),
    path('deleteECEF/<str:pk>/',deleteECEF.as_view()),
    path('updatecivilf/<str:pk>/',updatecivilf.as_view()),
    path('deletecsefa/<str:pk>/',deletecsefa.as_view()),
    path('updatecseup/<str:pk>/',updatecseup.as_view()),
    path('deleteece/<str:pk>/',deleteece.as_view()),
    path('updatefece/<str:pk>/',updatefece.as_view()),
    path('deletefeee/<str:pk>/',deletefeee.as_view()),
    path('updatefeee/<str:pk>/',updatefeee.as_view()),
    path('deletefme/<str:pk>/',deletefme.as_view()),
    path('updatefme/<str:pk>/',updatefme.as_view()),
    path('studentlogin/',views.studentlogin),
    # path('studentrolle/',views.studentrolle),
    path('logout/',views.studentlogout),
    path('civilstudents/',civilstudents.as_view(template_name="admin.html"),name='civil'),
    path('csestudentlist/',csestudentlist.as_view(template_name="admin.html"),name='cse'),
    path('eceliststudents/',eceliststudents.as_view(template_name="admin.html"),name='ece'),
    path('eeeliststudents/',eeeliststudents.as_view(template_name="admin.html"),name='eee'),
    path('mecliststudents/',mecliststudents.as_view(template_name="admin.html"),name='me'),
    path('deletemassege/<str:pk>/',deletemassege.as_view()),
    path('updatemassegs/<str:pk>/',updatemassegs.as_view()),
    path('deletecivil/<str:pk>/',deletecivil.as_view()),
    path('updatescivil/<str:pk>/',updatescivil.as_view()),
    path('updateCSEstudent/<str:pk>/',updateCSEstudent.as_view()),
    path('deletecse/<str:pk>/',deletecse.as_view()),
    path('upadateece/<str:pk>/',upadateece.as_view()),
    path('Deleteece/<str:pk>/',Deleteece.as_view()),
    path('updateseee/<str:pk>/',updateseee.as_view()),
    path('deleteeee/<str:pk>/',deleteeee.as_view()),
    path('updatesme/<str:pk>/',updatesme.as_view()),
    path('deleteme/<str:pk>/',deleteme.as_view()),





    path('civilstudentsregistation/',views.civilstudentsregistation),
    path('listcsestudentsregistation/',views.listcsestudentsregistation),
    path('eceliststudentsregistation/',views.eceliststudentsregistation),
    path('eeeliststudentsregistation/',views.eeeliststudentsregistation),
    path('mecliststudentsregistation/',views.mecliststudentsregistation),
    path('mecliststudentsregistation/',views.mecliststudentsregistation),
    path('civilregg/',views.civilregg),
    path('cseregg/',views.cseregg),
    path('eceregg/',views.eceregg),
    path('eeeregg/',views.eeeregg),
    path('mecregg/',views.mecregg),

    path('ECEstudent/',views.ECEstudent),
    path('EEEstudent/',views.EEEstudent),
    path('CSEstudent/',views.CSEstudent),
    path('CIVILstudents/',views.CIVILstudents),
    path('MEstudents/',views.MEstudents),


    path('ECErolle/',views.ECErolle),
    path('Civilrolleno/',views.Civilrolleno),
    path('merolleno/',views.merolleno),
    path('cserolleno/',views.cserolleno),
    path('eeerolleno/',views.eeerolleno),
    path('adminhomepage/',views.adminhomepage),
    path('Adminhomepage/',views.Adminhomepage),
    path('useraccount/',views.useraccount),
    path('reviews/',reviews.as_view(template_name="admin.html"),name='name'),
    path('openreviews/',openreviews.as_view(template_name="index.html"),name='name'),

]
