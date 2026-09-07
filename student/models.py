from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    Course_name = models.CharField(max_length=100)
    Course_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    faculty_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.Course_name


class Department(models.Model):
    Department_name = models.CharField(max_length=100)
    Department_code= models.CharField(max_length=20, unique=True)
    Suparviour_name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Department_name