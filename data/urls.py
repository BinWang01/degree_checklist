from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("colleges/", views.college_list, name="college_list"),
    path("colleges/<int:pk>/", views.college_edit, name="college_edit"),
    path("colleges/new/", views.college_edit, name="college_create"),
    path("departments/", views.department_list, name="department_list"),
    path("departments/<int:pk>/", views.department_edit, name="department_edit"),
    path("departments/new/", views.department_edit, name="department_create"),
    path("degrees/", views.degree_list, name="degree_list"),
    path("degrees/<int:pk>/", views.degree_edit, name="degree_edit"),
    path("degrees/new/", views.degree_edit, name="degree_create"),
    path("areas/", views.area_list, name="area_list"),
    path("areas/<int:pk>/", views.area_edit, name="area_edit"),
    path("areas/new/", views.area_edit, name="area_create"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_edit, name="course_edit"),
    path("courses/new/", views.course_edit, name="course_create"),
    path("areacourses/", views.area_course_list, name="area_course_list"),
    path("areacourses/<int:pk>/", views.area_course_edit, name="area_course_edit"),
    path("areacourses/new/", views.area_course_edit, name="area_course_create"),
]