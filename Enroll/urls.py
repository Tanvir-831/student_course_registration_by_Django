from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student-info/<int:student_id>/', views.student_info, name='student_info'),
    path('student-info/<int:student_id>/update-courses/', views.update_course, name='update_course'),
    path('student-info/<int:student_id>/remove-course/<str:course_id>', views.remove_course, name='remove_course')
]