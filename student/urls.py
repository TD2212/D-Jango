from django.urls import path
from . import views
from .views import CourseCreateView, CourseUpdateView

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("course/", views.course, name="course"),
    path("contact/", views.contact, name="contact"),
    path("result/", views.result, name="result"),
    path("student/", views.student_list, name="student_list"),
    path("student/add/", views.student_add, name="student_add"),
    path("student/edit/<int:id>/", views.student_edit, name="student_edit"),
    path("student/delete/<int:id>/", views.student_delete, name="student_delete"),
    path("course/list/", views.course_list, name="course_list"),
    path("course/add/", views.course_add, name="course_add"),
    path("course/edit/<int:id>/", CourseUpdateView.as_view(), name="course_edit"),
    path("course/delete/<int:id>/", views.course_delete, name="course_delete"),
    path("department_list/", views.department_list, name="department_list"),
]
