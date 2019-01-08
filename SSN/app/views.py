from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, DeleteView,RedirectView

# Create your views here.
from app.models import Civilfaculty, CSE, ECE, EEE, ME, Civilstudent, Csestudent, Ecestudent, Eeestudent, Mestudent, \
    usermessage


def showindex(request):
    return render(request,"index.html",{"type":"homedata"})

def openHomePage(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})
def openssnabout(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def Admissions(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Ssnfrees(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Shcolarship(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Acadamics(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Program(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def shchedual(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Examination(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Awards(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Civil(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Since(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Electronics(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Electrical(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Mechanical(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Rules(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def malparc(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Result(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def google(request):
    return redirect("https://www.google.co.in/search?q=r13+jntuk+results&rlz=1C1CHBD_enIN820IN820&oq=r13+jntuk&aqs=chrome.2.69i57j0l5.10536j0j7&sourceid=chrome&ie=UTF-8")


def Departments(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Dcivil(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DSince(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectronics(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DMechanical(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Dprogramsc(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Dstudentc(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Dgalleryc(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DSincep(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DSincesa(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DSincepg(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectronicsp(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectronicssa(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectronicsga(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectricalpo(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectrical(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectricalsd(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DElectricalga(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DMechanicalpo(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DMechanicalsd(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def DMechanicalga(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Admin(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def adminlogin(request):
    name=request.POST.get("username")
    apassword=request.POST.get("userpassword")
    if name == "mahesh" and apassword == "123456":
        return render(request,"admin.html")
    else:
        type= "Admin"
        return render(request,"index.html",{"type":type,"msg":"invalide username and password"})


def logout(request):
    return render(request,"index.html")


def studentregistation(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})



# class StudentDetailslist(ListView):
#     model = Student


def facultyregistation(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})


def civilregistation(request):
    type = request.GET.get("type")
    p3 = Civilfaculty.objects.last()
    id = 0
    if p3 == None:
        id = 101
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def civildetails(request):
    type = "civilregistation"
    name=request.POST.get("f1")
    idno=request.POST.get("f2")
    qulifi=request.POST.get("f3")
    reaserch=request.POST.get("f4")
    exp=request.POST.get("f5")
    dob=request.POST.get("f6")
    civil=Civilfaculty(name=name,idno=idno,qualiufi=qulifi,reasearch=reaserch,exp=exp,dob=dob)
    civil.save()
    return render(request,"admin.html",{"type":type,"msg3":"registered"})


def cseregistation(request):
    type = request.GET.get("type")
    p1 = CSE.objects.all()
    p3 = CSE.objects.last()
    id = 0
    if p3 == None:
        id = 201
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def cseregistationdetails(request):
    type = "cseregistation"
    name=request.POST.get("f1")
    idno=request.POST.get("f2")
    qulifi=request.POST.get("f3")
    reaserch=request.POST.get("f4")
    exp=request.POST.get("f5")
    dob=request.POST.get("f6")
    civil=CSE(name=name,idno=idno,qualiufi=qulifi,reasearch=reaserch,exp=exp,dob=dob)
    civil.save()
    return render(request,"admin.html",{"type":type,"msg3":"registered"})


def eceregistation(request):
    type = request.GET.get("type")
    p1 = ECE.objects.all()
    p3 = ECE.objects.last()
    id = 0
    if p3 == None:
        id = 301
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def eceregistationdetails(request):
    type = "eceregistation"
    name=request.POST.get("f1")
    idno=request.POST.get("f2")
    qulifi=request.POST.get("f3")
    reaserch=request.POST.get("f4")
    exp=request.POST.get("f5")
    dob=request.POST.get("f6")
    civil=ECE(name=name,idno=idno,qualiufi=qulifi,reasearch=reaserch,exp=exp,dob=dob)
    civil.save()
    return render(request,"admin.html",{"type":type,"msg3":"registered"})


def eeeregistation(request):
    type = request.GET.get("type")
    p1 = EEE.objects.all()
    p3 = EEE.objects.last()
    id = 0
    if p3 == None:
        id = 401
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def saveeee(request):
    type = "eeeregistation"
    name=request.POST.get("f1")
    idno=request.POST.get("f2")
    qulifi=request.POST.get("f3")
    reaserch=request.POST.get("f4")
    exp=request.POST.get("f5")
    dob=request.POST.get("f6")
    civil=EEE(name=name,idno=idno,qualiufi=qulifi,reasearch=reaserch,exp=exp,dob=dob)
    civil.save()
    return render(request,"admin.html",{"type":type,"msg3":"registered"})


def mecregistation(request):
    type = request.GET.get("type")
    p1 = ME.objects.all()
    p3 = ME.objects.last()
    id = 0
    if p3 == None:
        id = 501
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def mecsavedeatails(request):
    type = "mecregistation"
    name = request.POST.get("f1")
    idno = request.POST.get("f2")
    qulifi = request.POST.get("f3")
    reaserch = request.POST.get("f4")
    exp = request.POST.get("f5")
    dob = request.POST.get("f6")

    civil = ME(name=name, idno=idno, qualiufi=qulifi, reasearch=reaserch, exp=exp, dob=dob)
    civil.save()
    return render(request, "admin.html", {"type": type, "msg3": "registered"})
class Facultiesdetails(ListView):
    model = Civilfaculty
    context_object_name = "listcivil"


def facaltylist(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})

class listcse(ListView):
    model = CSE
    context_object_name = "listcse"

class ecelist(ListView):
    model = ECE
    context_object_name = "listece"
class eeelist(ListView):
    model = EEE
    context_object_name = "listeee"
class meclist(ListView):
    model = ME
    context_object_name = "listme"
class Dfacultycivil(ListView):
    model = Civilfaculty
    template_name = 'index.html'
class DSincefa(ListView):
    model = CSE
    template_name = 'index.html'
class DElectronicsf(ListView):
    model = ECE
    template_name = "index.html"
class DElectricals(ListView):
    model = EEE
    template_name = 'index.html'

class DMechanicalfd(ListView):
    model = ME
    template_name = 'index.html'
class updateECEF(UpdateView):
    model = ECE
    fields = '__all__'
    success_url = reverse_lazy('ecef')
class deleteECEF(DeleteView):
    model = ECE
    success_url = reverse_lazy('ecef')
class deleteEEE(DeleteView):
    model = EEE
    success_url = reverse_lazy('eeef')
class updatecEEE(UpdateView):
    model = EEE
    fields = "__all__"
    success_url = reverse_lazy('eeef')
class deleteME(DeleteView):
    model = ME
    success_url = reverse_lazy('mef')
class updateME(UpdateView):
    model = ME
    fields = '__all__'
    success_url = reverse_lazy('mef')

def Compus(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def boysgirl(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def hostellibrary(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Transport(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def sports(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Training(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Abouttap(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Placements(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Contact(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def Back(request):
    return render(request,"admin.html")
# class deletes(DeleteView):
#     model = Student
#     success_url = reverse_lazy('name')

# class updates(UpdateView):
#     model = Student
#     fields = '__all__'
#     success_url = reverse_lazy('name')
class deletecivilf(DeleteView):
    model = Civilfaculty
    success_url = reverse_lazy('civilf')
class updatecivilf(UpdateView):
    model = Civilfaculty
    fields = '__all__'
    success_url = reverse_lazy('civilf')
class deletecsefa(DeleteView):
    model = CSE
    success_url = reverse_lazy('csef')
class updatecseup(UpdateView):
    model = CSE
    fields = '__all__'
    success_url = reverse_lazy('csef')
class deleteece(DeleteView):
    model = ECE
    success_url = reverse_lazy('ece')
class updatefece(UpdateView):
    model = ECE
    fields = '__all__'
    success_url = reverse_lazy('ece')
class deletefeee(DeleteView):
    model = EEE
    success_url = reverse_lazy('eee')
class updatefeee(UpdateView):
    model = EEE
    fields = '__all__'
    success_url = reverse_lazy('eee')
class deletefme(DeleteView):
    model = ME
    success_url = reverse_lazy('me')
class updatefme(UpdateView):
    model = ME
    fields = '__all__'
    success_url = reverse_lazy('me')


def studentlogin(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


# def studentrolle(request):
#     name = request.POST.get("username")
#     apassword = request.POST.get("userpassword")
#     res=Student.objects.filter(rolleno=name,name=apassword)
#     if res:
#         return render(request, "studentprofile.html",{"res":res})
#     else:
#         type='studentlogin'
#         return render(request, "index.html",{"type":type,"msg7":'invlide'})


def studentlogout(request):
    return render(request,"index.html")


def studentdetails(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})
class civilstudents(ListView):
    model = Civilstudent
    context_object_name = "civillist"
class csestudentlist(ListView):
    model = Csestudent
    context_object_name = "cselist"
class eceliststudents(ListView):
    model = Ecestudent
    context_object_name = "ecelist"
class eeeliststudents(ListView):
    model = Eeestudent
    context_object_name = "eeelist"
class mecliststudents(ListView):
    model = Mestudent
    context_object_name = "melist"
class deletecivil(DeleteView):
    model = Civilstudent
    success_url = reverse_lazy('civil')
class deletecse(DeleteView):
    model = Csestudent
    success_url = reverse_lazy('cse')
class upadateece(UpdateView):
    model = Ecestudent
    fields = '__all__'
    success_url = reverse_lazy('ece')
class Deleteece(DeleteView):
    model = Ecestudent
    success_url = reverse_lazy('ece')
class updateseee(UpdateView):
    model = Eeestudent
    fields = '__all__'
    success_url = reverse_lazy('eee')
class deleteeee(DeleteView):
    model = Eeestudent
    success_url = reverse_lazy('eee')
class updatesme(UpdateView):
    model = Mestudent
    fields = '__all__'
    success_url = reverse_lazy('me')
class deleteme(DeleteView):
    model = Mestudent
    success_url = reverse_lazy('me')

class updatescivil(UpdateView):
    model = Civilstudent
    fields = '__all__'
    success_url = reverse_lazy('civil')
class updateCSEstudent(UpdateView):
    model = Csestudent
    fields = '__all__'
    #context_object_name = 'updatecse'
    success_url = reverse_lazy('cse')


class getecelist(ListView):
    model = Ecestudent
    template_name = 'admin.html'
    context_object_name = 'ecedata'



def civilstudentsregistation(request):
    type = request.GET.get("type")
    p3 = Civilstudent.objects.last()
    id = 0
    if p3 == None:
        id = 137111401
    else:
        id = p3.rolleno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def listcsestudentsregistation(request):
    type = request.GET.get("type")
    p3 = Csestudent.objects.last()
    id = 0
    if p3 == None:
        id = 137111501
    else:
        id = p3.rolleno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def eceliststudentsregistation(request):
    type = request.GET.get("type")
    p3 = Ecestudent.objects.last()
    id = 0
    if p3 == None:
        id = 137111601
    else:
        id = p3.rolleno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def eeeliststudentsregistation(request):
    type = request.GET.get("type")
    p1 = Eeestudent.objects.all()
    p3 = Eeestudent.objects.last()
    id = 0
    if p3 == None:
        id = 137111701
    else:
        id = p3.rolleno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})


def mecliststudentsregistation(request):
    type = request.GET.get("type")
    p3 = Mestudent.objects.last()
    id = 0
    if p3 == None:
        id = 137111801
    else:
        id = p3.rolleno
        id = (int(id) + 1)
    return render(request, "admin.html", {"type": type,"nam":id})



def civilregg(request):
    name = request.POST.get("t1")
    fname = request.POST.get("t2")
    course = request.POST.get("t3")
    rolleno = request.POST.get("t4")
    section = request.POST.get("t5")
    fristyearsub = request.POST.get("y9")
    secondyearsub = request.POST.get("y10")
    thardyearsub = request.POST.get("y11")
    fourthyaersub = request.POST.get("y12")
    persentage = request.POST.get("y13")
    student = Civilstudent(name=name, fname=fname, course=course, rolleno=rolleno, secation=section,fsub=fristyearsub,
                          ssub=secondyearsub, tsub=thardyearsub, fosub=fourthyaersub, Attendence=persentage)
    student.save()
    type="civilstudentsregistation"
    return render(request, "admin.html", {"msg2": "Registered","type":type})

def cseregg(request):
    name = request.POST.get("t1")
    fname = request.POST.get("t2")
    course = request.POST.get("t3")
    rolleno = request.POST.get("t4")
    section = request.POST.get("t5")
    fristyearsub = request.POST.get("y9")
    secondyearsub = request.POST.get("y10")
    thardyearsub = request.POST.get("y11")
    fourthyaersub = request.POST.get("y12")
    persentage = request.POST.get("y13")
    student = Csestudent(name=name, fname=fname, course=course, rolleno=rolleno, secation=section,fsub=fristyearsub,
                          ssub=secondyearsub, tsub=thardyearsub, fosub=fourthyaersub, Attendence=persentage)
    student.save()
    type="listcsestudentsregistation"
    return render(request, "admin.html", {"msg2": "Registered","type":type})

def eceregg(request):
    name = request.POST.get("t1")
    fname = request.POST.get("t2")
    course = request.POST.get("t3")
    rolleno = request.POST.get("t4")
    section = request.POST.get("t5")
    fristyearsub = request.POST.get("y9")
    secondyearsub = request.POST.get("y10")
    thardyearsub = request.POST.get("y11")
    fourthyaersub = request.POST.get("y12")
    persentage = request.POST.get("y13")
    student = Ecestudent(name=name, fname=fname, course=course, rolleno=rolleno, secation=section, fsub=fristyearsub,
                           ssub=secondyearsub, tsub=thardyearsub, fosub=fourthyaersub, Attendence=persentage)
    student.save()
    type = "eceliststudentsregistation"
    return render(request, "admin.html", {"msg2": "Registered", "type": type})


def eeeregg(request):
    name = request.POST.get("t1")
    fname = request.POST.get("t2")
    course = request.POST.get("t3")
    rolleno = request.POST.get("t4")
    section = request.POST.get("t5")
    fristyearsub = request.POST.get("y9")
    secondyearsub = request.POST.get("y10")
    thardyearsub = request.POST.get("y11")
    fourthyaersub = request.POST.get("y12")
    persentage = request.POST.get("y13")
    student = Eeestudent(name=name, fname=fname, course=course, rolleno=rolleno, secation=section, fsub=fristyearsub,
                           ssub=secondyearsub, tsub=thardyearsub, fosub=fourthyaersub, Attendence=persentage)
    student.save()
    type = "eeeliststudentsregistation"
    return render(request, "admin.html", {"msg2": "Registered", "type": type})


def mecregg(request):
    name = request.POST.get("t1")
    fname = request.POST.get("t2")
    course = request.POST.get("t3")
    rolleno = request.POST.get("t4")
    section = request.POST.get("t5")
    fristyearsub = request.POST.get("y9")
    secondyearsub = request.POST.get("y10")
    thardyearsub = request.POST.get("y11")
    fourthyaersub = request.POST.get("y12")
    persentage = request.POST.get("y13")
    student = Mestudent(name=name, fname=fname, course=course, rolleno=rolleno, secation=section, fsub=fristyearsub,
                           ssub=secondyearsub, tsub=thardyearsub, fosub=fourthyaersub, Attendence=persentage)
    student.save()
    type = "mecliststudentsregistation"
    return render(request, "admin.html", {"msg2": "Registered", "type": type})


def ECEstudent(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def EEEstudent(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def CSEstudent(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def CIVILstudents(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def MEstudents(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})


def ECErolle(request):
    name=request.POST.get("username")
    password=request.POST.get("userpassword")
    eced=Ecestudent.objects.filter(name=name,rolleno=password)
    if eced:
        type='ecestudentprofile'
        return render(request,"index.html",{"type":type,"ece":eced})
    else:
        type='ECEstudent'
        return render(request,"index.html",{"type":type,"msg1":"invalide rolleno"})


def Civilrolleno(request):
    name = request.POST.get("username")
    password = request.POST.get("userpassword")
    eced = Civilstudent.objects.filter(name=name, rolleno=password)
    if eced:
        type = 'civilstidentprofile'
        return render(request, "index.html", {"type": type, "ece": eced})
    else:
        type = 'CIVILstudents'
        return render(request, "index.html", {"type": type, "msg7": "invalide rolleno"})


def merolleno(request):
    name = request.POST.get("username")
    password = request.POST.get("userpassword")
    eced = Mestudent.objects.filter(name=name, rolleno=password)
    if eced:
        type = 'mestudentprofiles'
        return render(request, "index.html", {"type": type, "ece": eced})
    else:
        type = 'MEstudents'
        return render(request, "index.html", {"type": type, "msg7": "invalide rolleno"})


def cserolleno(request):
    name = request.POST.get("username")
    password = request.POST.get("userpassword")
    eced = Csestudent.objects.filter(name=name, rolleno=password)
    if eced:
        type = 'csestudentprofile'
        return render(request, "index.html", {"type": type, "ece": eced})
    else:
        type = 'CSEstudent'
        return render(request, "index.html", {"type": type, "msg7": "invalide rolleno"})


def eeerolleno(request):
    name = request.POST.get("username")
    password = request.POST.get("userpassword")
    eced = Eeestudent.objects.filter(name=name, rolleno=password)
    if eced:
        type = 'csestudentprofile'
        return render(request, "index.html", {"type": type, "ece": eced})
    else:
        type = 'EEEstudent'
        return render(request, "index.html", {"type": type, "msg7": "invalide rolleno"})


def adminhomepage(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})


def Adminhomepage(request):
    type = request.GET.get("type")
    return render(request, "admin.html", {"type": type})


def useraccount(request):
    name=request.POST.get("name")
    contact=request.POST.get("contact")
    email=request.POST.get("email")
    message=request.POST.get("message")
    mmm=usermessage.objects.filter(email=email)
    if mmm:
        type = "Contact"
        return render(request,"index.html",{"type":type,"msa0":"already use the email id "})
    else:
        mmm=usermessage(name=name,contact=contact,email=email,massege=message)
        mmm.save()
        type="Contact"
        return render(request,"index.html",{"type":type,"msg9":"save feedback"})
class reviews(ListView):
    model = usermessage
    context_object_name = "massege"
class deletemassege(DeleteView):
    model = usermessage
    success_url = reverse_lazy("name")
class updatemassegs(UpdateView):
    model = usermessage
    fields = '__all__'
    success_url = reverse_lazy("name")
class openreviews(ListView):
    model = usermessage
    context_object_name = "masseges"

