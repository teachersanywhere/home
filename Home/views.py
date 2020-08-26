from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Location, Teacher
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def findTeacher(request):
    context = {
        "location": Location.objects.all()
    }
    return render(request, "home/findTeacher.html", context)

def showTeacher(request):
    area = request.POST['pincode']
    location = Location.objects.get(area=area)
    teachers = []
    for obj in Teacher.objects.filter(location=location):
        teachers.append(obj)

    context = {
        'teachers': teachers 
    }

    return render(request, "home/showTeacher.html", context)

def contact(request):
    return render(request, "home/contact.html")

def profile(request, teacher_id):
    context = {
        "data": Teacher.objects.get(pk=teacher_id)
    }

    return render(request, "home/profile.html", context)