from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("findTeacher", views.findTeacher, name="findTeacher"),
    path("showTeacher", views.showTeacher, name="showTeacher"),
    path("contact", views.contact, name="contact"),
    path("profile/<int:teacher_id>", views.profile, name="profile"),
    path("courses", views.courses, name="courses"),
    path("coding/<int:class_id>", views.coding, name="coding")
]