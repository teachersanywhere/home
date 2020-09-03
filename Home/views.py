from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Location, Teacher, Subject
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def findTeacher(request):
    context = {
        "location": Location.objects.all(),
        "subjects": Subject.objects.all() 
    }
    return render(request, "home/findTeacher.html", context)

def showTeacher(request):
    area = request.POST['pincode']
    classes = request.POST['class-filter']
    subject = request.POST['subject-filter']
    sb = Subject.objects.get(subject=subject)
    location = Location.objects.get(area=area)
    teachers = []
    final = []
    for obj in Teacher.objects.filter(location=location):
        teachers.append(obj)

    for t in teachers:
        if t.classes == classes:
            if t.subject1 == sb or t.subject2 == sb or t.subject3 == sb:
                final.append(t)
                

    context = {
        'teachers': final
    }

    return render(request, "home/showTeacher.html", context)

def contact(request):
    return render(request, "home/contact.html")

def profile(request, teacher_id):
    context = {
        "data": Teacher.objects.get(pk=teacher_id)
    }

    return render(request, "home/profile.html", context)

def courses(request):
    return render(request, "home/courses.html")

def coding(request, class_id):
    if class_id == 6:
        return render(request, "home/class6.html")
    elif class_id == 7:
        return render(request, "home/class7.html")
    elif class_id == 8:
        return render(request, "home/class8.html")
    else:
        return HttpResponse('Not Found')