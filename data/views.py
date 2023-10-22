from django.shortcuts import render
from django.http import HttpResponse
from data.models import College, Department, Degree, Area, Course, Area_Course
from django.shortcuts import render, get_object_or_404, redirect
from data.forms import CollegeForm, DepartmentForm, DegreeForm, AreaForm, CourseForm, AreaCourseForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def index(request):
    area_courses = Area_Course.objects.select_related("course").select_related("area").all()
    return render(request,"index.html",{'items':area_courses})

def college_list(request):
    colleges = College.objects.all()
    return render(request,"college/college-list.html",{'colleges':colleges})

def college_edit(request, pk=None):
    if pk is not None:
        college = get_object_or_404(College, pk=pk)
    else:
        college = None

    if request.method == "POST":
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid():
            updated_college = form.save()
            if college is None:
                messages.success(
                    request, 'College "{}" was created.'.format(updated_college)
                )
            else:
                messages.success(
                    request, 'College "{}" was updated.'.format(updated_college)
                )

            return redirect("college_list")
    else:
        form = CollegeForm(instance=college)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "College",
            "instance": college,
        },
    )

def department_list(request):
    departments = Department.objects.select_related("college").all()
    return render(request,"department/department-list.html",{'departments':departments})

def department_edit(request, pk=None):
    if pk is not None:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            updated_department = form.save()
            if department is None:
                messages.success(
                    request, 'Department "{}" was created.'.format(updated_department)
                )
            else:
                messages.success(
                    request, 'Department "{}" was updated.'.format(updated_department)
                )

            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Department",
            "instance": department,
        },
    )

def degree_list(request):
    degrees = Degree.objects.select_related("department").all()
    return render(request,"degree/degree-list.html",{'degrees':degrees})

def degree_edit(request, pk=None):
    if pk is not None:
        degree = get_object_or_404(Degree, pk=pk)
    else:
        degree = None

    if request.method == "POST":
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            updated_degree = form.save()
            if degree is None:
                messages.success(
                    request, 'Degree "{}" was created.'.format(updated_degree)
                )
            else:
                messages.success(
                    request, 'Degree "{}" was updated.'.format(updated_degree)
                )

            return redirect("degree_list")
    else:
        form = DegreeForm(instance=degree)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Degree",
            "instance": degree,
        },
    )


def area_list(request):
    areas = Area.objects.select_related("degree").all()
    return render(request,"area/area-list.html",{'areas':areas})

def area_edit(request, pk=None):
    if pk is not None:
        area = get_object_or_404(Area, pk=pk)
    else:
        area = None

    if request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            updated_area = form.save()
            if area is None:
                messages.success(
                    request, 'Area "{}" was created.'.format(updated_area)
                )
            else:
                messages.success(
                    request, 'Area "{}" was updated.'.format(updated_area)
                )

            return redirect("area_list")
    else:
        form = AreaForm(instance=area)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Area",
            "instance": area,
        },
    )

def course_list(request):
    courses = Course.objects.all()
    return render(request,"course/course-list.html",{'courses':courses})

def course_edit(request, pk=None):
    if pk is not None:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            updated_course = form.save()
            if course is None:
                messages.success(
                    request, 'Course "{}" was created.'.format(updated_course)
                )
            else:
                messages.success(
                    request, 'Course "{}" was updated.'.format(updated_course)
                )

            return redirect("course_list")
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Course",
            "instance": course,
        },
    )

def area_course_list(request):
    area_courses = Area_Course.objects.select_related("course").select_related("area").all()
    return render(request,"areacourse/area-course-list.html",{'areacourses':area_courses})

def area_course_edit(request, pk=None):
    if pk is not None:
        areacourse = get_object_or_404(Area_Course, pk=pk)
    else:
        areacourse = None

    if request.method == "POST":
        form = AreaCourseForm(request.POST, instance=areacourse)
        if form.is_valid():
            updated_areacourse = form.save()
            if areacourse is None:
                messages.success(
                    request, 'Area Course "{}" was created.'.format(updated_areacourse)
                )
            else:
                messages.success(
                    request, 'Area Course "{}" was updated.'.format(updated_areacourse)
                )

            return redirect("area_course_list")
    else:
        form = AreaCourseForm(instance=areacourse)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "AreaCourse",
            "instance": areacourse,
        },
    )