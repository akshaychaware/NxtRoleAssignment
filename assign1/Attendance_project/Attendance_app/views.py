from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("hii from django views")


def add_student(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        student_class=request.POST.get('student_class')
        email=request.POST.get('email')
        Student.objects.create(
            name=name,
            roll_no=roll_no,
            student_class=student_class,
            email=email
        )
        return redirect('studentlist')
    return render(request,'add_student.html')


def student_list(request):
    students=Student.objects.all()

    return render(request,'student_list.html',{'students':students})

def updatestudent(request,id):
    if request.method == 'POST':
        Student.objects.filter(id=id).update(
            name=request.POST.get('name'),
            roll_no=request.POST.get('roll_no'),
            student_class=request.POST.get('student_class'),
            email=request.POST.get('email')
        )
        return redirect('studentlist')
    students=Student.objects.filter(id=id).first()
    return render(request,'add_student.html',{'students':students})

    
        
def deletestudent(request,id):
    Student.objects.filter(id=id).delete()
    return redirect('studentlist')

