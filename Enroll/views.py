from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
# Create your views here.
def home(request):
    all_courses = Course.objects.all()

    if request.method =='GET':
        search_query = request.GET.get('student_id')
        if search_query:
            student = Student.objects.get(student_id=search_query)
            return redirect('student_info', student_id=student.id)
    return render(request, 'home.html', {'courses': all_courses})


def student_info(request, student_id):

    student = get_object_or_404(Student, pk=student_id)
    registered_courses = student.courses.all()

    return render(request, 'student_info.html', {'student': student, 'registered_courses': registered_courses})


def update_course(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    registered_courses = student.courses.all()
    available_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        action = request.POST.get('action')
        selected_course_id = request.POST.get('course_id')

        course = Course.objects.get(course_id=selected_course_id)
        student.courses.add(course)
        return redirect('student_info', student_id=student.id)

    return render(request, 'update_course.html', {'student': student, 'registered_courses': registered_courses, 'available_courses': available_courses})


def remove_course(request, student_id, course_id):
    student = get_object_or_404(Student, student_id=student_id)
    course = get_object_or_404(Course, course_id=course_id)
    if course in student.courses.all():
        student.courses.remove(course)
    return redirect('student_info', student_id=student.id)
