
from django.db import models
 
# Create your models here.
 
class Course(models.Model):
 
    COURSE_THEORY = 'Theory'
    COURSE_LAB = 'Lab'
    COURSE_PROJECT = 'Project'
    COURSE_CHOICES = [
        (COURSE_THEORY, 'Theory'),
        (COURSE_LAB, 'Lab'),
        (COURSE_PROJECT, 'Project')
    ]
 
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=40)
    course_credit = models.DecimalField(max_digits=4, decimal_places=2)
    tutorial_full_marks = models.DecimalField(max_digits=4, decimal_places=2)
    att_full_marks = models.DecimalField(max_digits=4, decimal_places=2)
    final_full_marks = models.DecimalField(max_digits=4, decimal_places=2)
    course_type = models.CharField(
        max_length=10,
        choices=COURSE_CHOICES,
        default=COURSE_THEORY
    )    
 
    def __str__(self):
        return self.course_id + ": " + self.course_name
    
 
 
class Student(models.Model):
    YEAR_CHOICES = [
        ('First', 'First Year 1st Semester'),
        ('First2', 'First Year 2nd Semester'),
        ('Second', 'Second Year 1st Semester'),
        ('Second2', 'Second Year 2nd Semester'),
        ('Third', 'Third Year 1st Semester'),
        ('Third2', 'Third Year 2nd Semester'),
        ('Fourth', 'Fourth Year 1st semster'),
        ('Fourth2', 'Fourth Year 2nd semster'),
    ]
    name = models.CharField(max_length=50)
    student_id = models.PositiveSmallIntegerField(unique=True)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, default='First')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
 
    def __str__(self):
        return "Name: (" + self.name + ") " + "Student ID: (" + str(self.student_id) + ")"
