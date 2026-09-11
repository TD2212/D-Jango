from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Student, Course ,Department
from .form import CourseForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth import *
from django.contrib.auth.decorators import *
from django.contrib.auth.mixins import *



# =========================
# STUDENT CRUD
# =========================

def student_list(request):
    students = Student.objects.all()

    return render(request, "studentCrud/list.html", {
        "students": students
    })


def student_add(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            mobile=request.POST.get("mobile"),
            city=request.POST.get("city")
        )

        return redirect("student_list")

    return render(request, "studentCrud/add.html")


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.mobile = request.POST.get("mobile")
        student.city = request.POST.get("city")

        student.save()

        return redirect("student_list")

    return render(request, "studentCrud/edit.html", {
        "student": student
    })


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "studentCrud/delete.html", {
        "student": student
    })


# =========================
# COURSE CRUD
# =========================

def course_list(request):
    courses = Course.objects.all()

    return render(request, "courseCrud/list.html", {
        "courses": courses
    })


def course_add(request):
    if request.method == "POST":
        try:
            Course.objects.create(
                Course_name=request.POST.get("Course_name"),
                Course_code=request.POST.get("Course_code"),
                start_date=request.POST.get("start_date"),
                end_date=request.POST.get("end_date"),
                faculty_name=request.POST.get("faculty_name"),
                is_active=request.POST.get("is_active") == "True"
            )

            return redirect("course_list")

        except IntegrityError:
            return render(request, "courseCrud/add.html", {
                "error": "Course code already exists."
            })

    return render(request, "courseCrud/add.html")


def course_edit(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        course.Course_name = request.POST.get("Course_name")
        course.Course_code = request.POST.get("Course_code")
        course.start_date = request.POST.get("start_date")
        course.end_date = request.POST.get("end_date")
        course.faculty_name = request.POST.get("faculty_name")
        course.is_active = request.POST.get("is_active") == "True"

        try:
            course.save()
            return redirect("course_list")

        except IntegrityError:
            return render(request, "courseCrud/edit.html", {
                "course": course,
                "error": "Course code already exists."
            })

    return render(request, "courseCrud/edit.html", {
        "course": course
    })


def course_delete(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "courseCrud/delete.html", {
        "course": course
    })


# =========================
# OTHER PAGES
# =========================



def home(request):
    username='Dabhi'
    return render(request, "home.html",{'username':username})


@login_required(login_url ='login')
def about(request):
    return render(request, "about.html")


def course(request):
    return redirect("course_list")


def contact(request):
    return render(request, "contact.html")


def student(request):
    return render(request, "student.html")


def result(request):
    return render(request, "result.html")

class CourseCreateView(CreateView):
    model=Course
    form_class=CourseForm
    template_name='courseCrud/add.html'
    success_url=reverse_lazy('courseCrud/list.html')


class CourseUpdateView(UpdateView):
    model=Course
    form_class=CourseForm
    template_name='courseCrud/add.html'
    success_url=reverse_lazy('courseCrud/list.html')

def department_list(request):
    departments = Department.objects.all()

    return render(
        request,
        'department_list.html',
        {'departments': departments}
    )

def login_view(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html',{
                'error':'Invalid username or Password'
            })   
    return render(request,'login.html')
            
def logout_view(request):
    logout(request)
    return redirect('login')